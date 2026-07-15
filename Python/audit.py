import boto3
import json
from pathlib import Path

iam = boto3.client("iam")
report = []

paginator = iam.get_paginator("list_users")

for page in paginator.paginate():
    for user in page["Users"]:
        username = user["UserName"]

        policies = iam.list_attached_user_policies(
            UserName=username
        )["AttachedPolicies"]

        policy_names = [
            policy["PolicyName"]
            for policy in policies
        ]

        report.append({
            "User": username,
            "AttachedPolicies": policy_names,
            "AdministratorAccess": "AdministratorAccess" in policy_names
        })

print(json.dumps(report, indent=4))

report_folder = Path(__file__).resolve().parent.parent / "Reports"
report_folder.mkdir(exist_ok=True)

report_file = report_folder / "report.json"

with report_file.open("w", encoding="utf-8") as file:
    json.dump(report, file, indent=4)

print("Audit completed successfully.")
print(f"Report saved to: {report_file}")
