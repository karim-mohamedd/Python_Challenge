from fpdf import FPDF

# Create PDF instance
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()


pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Infrastructure Internship Preparation Guide", ln=True, align="C")


pdf.ln(10)


pdf.set_font("Arial", size=12)

# Questions and answers
content = [
    ("1. What is Infrastructure as Code (IaC)? Can you name some tools used for IaC?", 
     "Infrastructure as Code (IaC) is the practice of managing and provisioning IT infrastructure through machine-readable configuration files, rather than manual processes. It allows for automation, consistency, and scalability. Some popular IaC tools are:\n- Terraform\n- Ansible\n- Puppet\n- Chef."),
    
    ("2. Can you explain the difference between Docker and Kubernetes?", 
     "Docker is a platform that allows you to containerize applications, making them easier to deploy and manage. Kubernetes is a container orchestration tool that helps manage large numbers of containers and automates deployment, scaling, and operations of containerized applications."),
    
    ("3. What is a CI/CD pipeline? Why is it important in DevOps?", 
     "CI/CD (Continuous Integration and Continuous Deployment) is a set of practices and tools to automatically build, test, and deploy code. It improves collaboration, speeds up software delivery, and reduces the risk of errors in production by automating repetitive tasks."),
    
    ("4. What is cloud computing? Can you explain the different types of cloud services (IaaS, PaaS, SaaS)?", 
     "Cloud computing is the delivery of computing resources over the internet. The three primary types of cloud services are:\n- IaaS (Infrastructure as a Service)\n- PaaS (Platform as a Service)\n- SaaS (Software as a Service)."),
    
    ("5. How does DNS work?", 
     "DNS (Domain Name System) translates human-readable domain names (like www.example.com) into IP addresses that computers use to identify each other. When you type a URL in a browser, it sends a DNS request to resolve the domain into an IP address."),
    
    ("6. What are the benefits of using version control systems like Git?", 
     "Git allows multiple developers to collaborate without overwriting each other's work. It tracks changes to code, making it easy to revert or compare versions. Git also enables branching and code review through pull requests."),
    
    ("7. Can you explain how Terraform works and why it is used?", 
     "Terraform is an IaC tool that automates cloud infrastructure provisioning using configuration files. It helps define, provision, and manage infrastructure across multiple cloud platforms like AWS, Azure, and GCP."),
    
    ("8. What is the difference between a Load Balancer and a Reverse Proxy?", 
     "A Load Balancer distributes incoming traffic across multiple servers to ensure no single server is overwhelmed, improving availability. A Reverse Proxy sits between the client and the server, forwarding requests to the appropriate server and providing additional functionalities like caching and SSL termination."),
    
    ("9. What is a Virtual Private Cloud (VPC), and why is it important?", 
     "A Virtual Private Cloud (VPC) is a private network in the cloud that allows you to control network settings (IP addresses, subnets, route tables). It provides isolation and ensures that only authorized users have access to network resources."),
    
    ("10. What are some monitoring tools you are familiar with, and why is monitoring important in infrastructure?", 
     "Some monitoring tools include:\n- Prometheus\n- Nagios\n- Grafana\n- CloudWatch\nMonitoring ensures the health and performance of infrastructure by detecting issues early, improving uptime, and optimizing performance."),
    
    ("11. What is the role of Automation in DevOps?", 
     "Automation in DevOps reduces manual intervention, increases consistency, and speeds up processes. It allows teams to automate infrastructure provisioning, CI/CD pipelines, testing, and deployment tasks."),
    
    ("12. What is a Virtual Machine (VM) and how does it differ from a container?", 
     "A VM is an emulation of a physical computer, running its own OS, while a container shares the host OS and is more lightweight. Containers are typically faster to start and consume fewer resources than VMs."),
    
    ("13. What is Scaling in cloud computing, and how does it work?", 
     "Scaling in cloud computing adjusts computational resources based on demand. Vertical scaling increases the power of a single instance, while horizontal scaling adds more instances to distribute the load. Auto-scaling automatically adjusts resources based on conditions like CPU usage."),
    
    ("14. What is the difference between a public cloud, private cloud, and hybrid cloud?", 
     "A public cloud is provided by third-party vendors (e.g., AWS), a private cloud is dedicated to a single organization, and a hybrid cloud combines both for more flexibility and optimization."),
    
    ("15. What are security best practices you should follow when managing cloud infrastructure?", 
     "Security best practices include using IAM roles, encrypting data, enabling MFA, patching systems regularly, using firewalls, and monitoring cloud usage through tools like CloudTrail."),
    
    ("16. What is a CDN (Content Delivery Network), and why is it used?", 
     "A CDN is a network of distributed servers that cache and deliver content to users based on their location. It improves website performance by reducing latency and speeding up load times."),
    
    ("17. How do you manage secrets (e.g., API keys, passwords) in a cloud environment?", 
     "Secrets management can be done using services like AWS Secrets Manager, Azure Key Vault, or by storing them as environment variables in the CI/CD pipeline. Data should be encrypted and access should follow the principle of least privilege."),
    
    ("18. What is a microservice architecture, and how does it benefit modern application deployment?", 
     "Microservices break down applications into smaller, independent services, improving scalability, resilience, and development speed. Each service can be deployed independently, leading to faster updates and maintenance."),
    
    ("19. Can you explain the concept of 'Infrastructure as a Service (IaaS)' in a cloud environment?", 
     "IaaS provides virtualized computing resources over the internet. Users rent virtual machines, storage, and networking resources, while the cloud provider manages the underlying hardware."),
    
    ("20. What are the advantages and disadvantages of using containers in development?", 
     "Advantages include consistency, portability, and fast startup. Disadvantages include security concerns, complexity in managing many containers, and challenges with data persistence."),
    
    ("21. What is Load Balancing, and why is it important in cloud infrastructure?", 
     "Load balancing distributes network traffic across multiple servers to ensure no server is overwhelmed. It increases availability and reliability by ensuring that if one server fails, others can handle the traffic."),
    
    ("22. What are the most common cloud service providers, and what do they offer?", 
     "Common cloud providers include AWS, Microsoft Azure, and Google Cloud, each offering computing, storage, networking, and database services."),
    
    ("23. Can you explain the difference between Stateful and Stateless services in cloud infrastructure?", 
     "Stateful services maintain state across requests (e.g., databases), while stateless services do not rely on previous interactions and are easier to scale."),
]

# Add the questions and answers to the PDF
for question, answer in content:
    pdf.set_font("Arial", 'B', 12)
    pdf.multi_cell(0, 10, txt=question)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=answer)
    pdf.ln(5)

# Output the PDF to a file
file_path = "c:/Users/ascom/Desktop/Infrastructure_Internship_Preparation_Guide.pdf"
pdf.output(file_path)

file_path


