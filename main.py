from pyscript import display

contact_info = {"Principal's Gmail": "gabrielle.damondamon@gmail.com",
                "Principal's Contact Phone" : "+63 954 443 0740",
                "School's Gmail" : "sdmu.manila@sanctusdemanila.edu.ph",
                "School's Contact Phone" : "+63 928 523 1234"}

display(f"Principal's Gmail: {contact_info["Principal's Gmail"]}", target="contact_info")
display(f"Principal's Contact Phone: {contact_info["Principal's Contact Phone"]}", target="contact_info")
display(f"School's Gmail: {contact_info["School's Gmail"]}", target="school_contact_info")
display(f"School's Contact Phone: {contact_info["School's Contact Phone"]}", target="school_contact_info")