cover_letter_template = """
I am excited to apply for the {role} position at {company_name}. With a strong foundation in backend development and a passion for crafting efficient and scalable systems, I am eager to contribute to your mission of creating innovative tools that empower developers to work smarter and faster.

In my journey as a software developer, I have worked on projects that combine backend expertise, system design, and impactful user experiences:

- Sociopedia: Developed a social media-like platform using the MERN stack, where I focused on backend development, including database design, secure user authentication, and API integration, ensuring a robust and scalable architecture.
- Sign Language Recognition System: Built a computer vision model integrated with a backend pipeline to handle real-time gesture recognition, demonstrating my ability to bridge AI solutions with reliable backend systems.
- Heart Disease Prediction: Created a machine learning pipeline to predict heart disease probabilities based on clinical data. I also implemented a backend API to process incoming data and provide seamless integration for end-user applications.

What excites me most about {company_name} is your commitment to enhancing developer workflows and productivity. Your focus on creating powerful, customizable tools aligns perfectly with my passion for building systems that deliver meaningful value to users.

My technical expertise includes Python, Node.js, Django, SQL, and MongoDB, along with experience in API development, data processing, and system optimization. I thrive in collaborative environments and excel at transforming complex challenges into elegant, maintainable solutions.

I am confident that my backend development experience, technical skill set, and enthusiasm for impactful software make me a strong candidate for this role. I would welcome the opportunity to discuss how I can contribute to {company_name}’s mission.

Thank you for considering my application. I look forward to the possibility of joining your team and helping {company_name} create tools that developers love.

Sincerely,  
Yash Dobriyal  
[GitHub Profile](https://github.com/SIGEGV)  
[Resume Link](https://drive.google.com/file/d/1NRLSv8JVOyH1cgRc1VsT_sj7Pk6xz0sf/view?usp=drive_link)
"""


def generate_cover_letter(company_name, role):
    cover_letter = cover_letter_template.format(company_name=company_name, role=role)
    return cover_letter

def main():
    company_name = input("Enter the company name: ")
    role = input("Enter the role you're applying for: ")
    
    cover_letter = generate_cover_letter(company_name, role)
    file_path = "cover_letter.txt"
    
    with open(file_path, "w") as file:
        file.write(cover_letter)
    
    print(f"Your cover letter has been saved to {file_path}")
    
if __name__ == "__main__":
    main()