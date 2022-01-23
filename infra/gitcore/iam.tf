resource "aws_iam_user" "github_user" {
  name = var.github_user
}

data "aws_iam_policy_document" "github_user_policy" {
  statement {
    actions = [
          "ecr:GetAuthorizationToken",
          "ecr:BatchCheckLayerAvailability",
          "ecr:GetDownloadUrlForLayer",
          "ecr:GetRepositoryPolicy",
          "ecr:DescribeRepositories",
          "ecr:BatchGetImage",
          "ecr:GetLifecyclePolicy",
          "ecr:GetLifecyclePolicyPreview",
          "ecr:ListTagsForResource",
          "ecr:DescribeImageScanFindings",
          "ecr:InitiateLayerUpload",
          "ecr:UploadLayerPart",
          "ecr:CompleteLayerUpload",
          "ecr:PutImage"
        ]
    resources = ["arn:aws:ecr:::*"]
    effect = "Allow"
  }
}

resource "aws_iam_policy" "github_user_policy" {
  name       = var.github_user_policy
  policy     = data.aws_iam_policy_document.github_user_policy.json
}

resource "aws_iam_user_policy_attachment" "github-user-attachment" {
  user       = aws_iam_user.github_user.name
  policy_arn = aws_iam_policy.github_user_policy.arn
}
