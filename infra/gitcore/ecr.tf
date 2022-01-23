resource "aws_ecr_repository" "nomad" {
  name                 = "nomad"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}
