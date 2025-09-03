# Configure the AWS provider
provider "aws" {
  region = "us-east-1" # change to your region
}

# Create IAM group
resource "aws_iam_group" "yash_group" {
  name = "yash_group"
}

# Attach AmazonS3ReadOnlyAccess policy to the group
resource "aws_iam_group_policy_attachment" "s3_readonly_attach" {
  group      = aws_iam_group.yash_group.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
}

# List of user names
variable "user_names" {
  default = ["yash1", "yash2", "yash3", "yash4"]
}

# Create IAM users
resource "aws_iam_user" "users" {
  for_each = toset(var.user_names)
  name     = each.key
}

# Add users to the group
resource "aws_iam_user_group_membership" "user_group_membership" {
  for_each = toset(var.user_names)
  user     = aws_iam_user.users[each.key].name
  groups   = [aws_iam_group.yash_group.name]
}
