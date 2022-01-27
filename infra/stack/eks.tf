module "label" {
  source = "cloudposse/label/null"

  name       = var.label_name
  attributes = ["cluster"]
}

locals {
  # Prior to Kubernetes 1.19, the usage of the specific kubernetes.io/cluster/* resource tags below are required
  # for EKS and Kubernetes to discover and manage networking resources
  # https://www.terraform.io/docs/providers/aws/guides/eks-getting-started.html#base-vpc-networking
  tags = { "kubernetes.io/cluster/${module.label.id}" = "shared" }
}

module "vpc" {
  source = "cloudposse/vpc/aws"

  cidr_block = "172.16.0.0/16"

  tags    = local.tags
  context = module.label.context
}

module "subnets" {
  source = "cloudposse/dynamic-subnets/aws"

  availability_zones   = var.availability_zones
  vpc_id               = module.vpc.vpc_id
  igw_id               = module.vpc.igw_id
  cidr_block           = module.vpc.vpc_cidr_block
  nat_gateway_enabled  = true
  nat_instance_enabled = false

  tags    = local.tags
  context = module.label.context
}

module "eks_cluster" {
  source = "cloudposse/eks-cluster/aws"
  region = var.region

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.subnets.public_subnet_ids

  kubernetes_version    = var.kubernetes_version
  oidc_provider_enabled = true

  context = module.label.context
}

module "eks_node_group" {
  source = "cloudposse/eks-node-group/aws"

  instance_types        = [var.instance_type]
  desired_size          = var.desired_size
  subnet_ids            = module.subnets.public_subnet_ids
  min_size              = var.min_size
  max_size              = var.max_size
  cluster_name          = module.eks_cluster.eks_cluster_id
  create_before_destroy = true
  kubernetes_version    = var.kubernetes_version == null || var.kubernetes_version == "" ? [] : [var.kubernetes_version]

  # Enable the Kubernetes cluster auto-scaler to find the auto-scaling group

  context = module.label.context

  # Ensure the cluster is fully created before trying to add the node group
  module_depends_on = [module.eks_cluster.kubernetes_config_map_id]
}
