resource "aws_iam_user" "test_user1" {
  name = "test-user-1"
}

resource "aws_iam_user" "test_user2" {
  name = "test-user-2"
}

resource "aws_iam_user_policy_attachment" "admin_access" {
  user       = aws_iam_user.test_user1.name
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
}

resource "aws_iam_user_policy_attachment" "read_only_access" {
  user       = aws_iam_user.test_user2.name
  policy_arn = "arn:aws:iam::aws:policy/ReadOnlyAccess"
}