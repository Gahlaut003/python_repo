from fpdf import FPDF

# Initialize the PDF object
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# # Add a Unicode-compatible font
# pdf.add_font("DejaVu", '', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', uni=True)
# pdf.set_font("DejaVu", size=12)

# Define the resume content
resume_content = """
Resume

[Your Full Name]
[Your Address]
[City, State, ZIP Code]
[Email Address] | [Phone Number] | [LinkedIn Profile] | [GitHub/Portfolio Link]

Objective
Highly skilled and experienced Senior Full Stack Developer with expertise in .NET, Angular, Google Cloud Platform (GCP), and Microsoft Azure. Adept at designing, developing, and deploying scalable, secure, and high-performance web applications. Seeking to contribute technical leadership and innovative solutions to drive organizational success.

Professional Experience

Senior Full Stack Developer
[Company Name], [City, State]
[MM/YYYY] – Present

- Designed, developed, and maintained end-to-end web applications using .NET Core, C#, and Angular for responsive and high-performing user interfaces.
- Deployed cloud-native solutions using GCP and Azure, leveraging services like App Engine, Azure App Services, Cloud Storage, and Cosmos DB.
- Built and optimized RESTful APIs and microservices for seamless integration with external systems.
- Led technical discussions and collaborated with cross-functional teams to define application architecture and ensure scalability and maintainability.
- Implemented CI/CD pipelines using Azure DevOps and GitHub Actions, automating build, test, and deployment workflows.
- Monitored application performance and resolved issues to maintain high availability and low latency.
- Mentored junior developers, conducted code reviews, and enforced coding standards and best practices.

Key Achievements:
- Successfully migrated a legacy monolithic application to a microservices-based architecture, reducing deployment times by 50%.
- Improved application performance by optimizing database queries and reducing API response times by 30%.

Full Stack Developer
[Previous Company Name], [City, State]
[MM/YYYY] – [MM/YYYY]

- Developed enterprise-level applications using ASP.NET MVC/Web API, Angular, and SQL Server.
- Integrated Azure cloud services such as Azure Functions, Logic Apps, and Key Vault to enhance application functionality.
- Worked on containerized applications using Docker and orchestrated deployments with Kubernetes.
- Conducted performance optimization and debugging to improve user experience and application reliability.
- Collaborated with stakeholders to gather requirements and deliver solutions within Agile workflows.

Key Achievements:
- Automated deployment processes, reducing manual intervention and improving deployment success rates by 40%.
- Contributed to the design and implementation of a multi-tenant architecture for SaaS applications.

Education

Bachelor of Science in Computer Science
[University Name], [City, State]
[Graduation Year]

Certifications

- Microsoft Certified: Azure Developer Associate
- Google Cloud Professional Cloud Developer
- Scrum Alliance Certified ScrumMaster (CSM)

Technical Skills

- Backend Technologies: .NET Core, ASP.NET MVC/Web API, C#, Entity Framework
- Frontend Technologies: Angular (10+), HTML5, CSS3, TypeScript, JavaScript, NgRx
- Cloud Platforms: Google Cloud Platform (GCP), Microsoft Azure
- DevOps Tools: Azure DevOps, GitHub Actions, Jenkins
- Databases: SQL Server, PostgreSQL, Cosmos DB, Cloud SQL
- Tools and Frameworks: Docker, Kubernetes, Swagger, Postman
- Other Skills: CI/CD pipelines, Microservices architecture, SOLID principles

Soft Skills

- Strong communication and collaboration skills
- Effective mentorship and leadership abilities
- Proactive problem-solving and critical thinking
- Adaptability and eagerness to learn new technologies

Projects

Multi-Tenant SaaS Platform
- Developed a cloud-native SaaS platform using .NET Core, Angular, and Azure.
- Implemented multi-tenancy with dynamic configurations based on tenant-specific requirements.

E-Commerce Web Application
- Built a scalable e-commerce solution with ASP.NET Core and Angular.
- Integrated payment gateways and optimized the checkout process for performance and security.

Professional Summary
With over [X years] of experience in full stack development, I bring a proven track record of delivering innovative, cloud-native solutions. My expertise in .NET, Angular, GCP, and Azure enables me to lead complex projects and drive successful outcomes. I thrive in collaborative environments and am committed to continuous learning and professional growth.
"""

# Add content to the PDF
for line in resume_content.split("\n"):
    pdf.multi_cell(0, 10, line)

# Save the PDF to a file
file_path = "/mnt/data/Senior_Full_Stack_Developer_Resume.pdf"
pdf.output(file_path)

file_path
