# mini-project-08-python-and-terraform-script
# Cloud Platform Analyzer + IAM Setup

This project combines **Python (boto3)** and **Terraform** to give you visibility into your AWS resources and to manage IAM users/groups.

---

## 🚀 Features

### Python Script (boto3)
- Lists all **EC2 Instances** with their state and IDs
- Shows **AMIs** owned by your account
- Displays **Launch Templates**
- Retrieves **Load Balancers** (Classic, Application, and Network)
- Lists all **Auto Scaling Groups**

### Terraform (IAM)
- Creates an IAM group called **`yash_group`**
- Creates **5 IAM users** (`yash1`, `yash2`, `yash3`, `yash4`, `yash5`)
- Adds all 5 users into **`yash_group`**
- Attaches **AmazonS3ReadOnlyAccess** policy to the group

---

## 🛠️ Requirements

- **AWS account** with IAM permissions
- **Python 3.x**
- **boto3** library
- **Terraform**

Install boto3 on Ubuntu:
```bash
sudo apt update
sudo apt install -y python3 python3-pip
pip3 install boto3 --break-system-packages
