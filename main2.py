from pyscript import display, document

#This entire code is divided into 3 different functions with different buttons with py-click, 
# because combining them will result into a reset without showing the results.  

def student_info(e): #This shows the student information
    last_name = str(document.getElementById("last_name").value)
    first_name = str(document.getElementById("first_name").value)
    
    display(f"Student Name: {last_name}, {first_name}", target = "student_info") #I put the display() function into two different parts.  

def calculate_gwa(e): #This code shows the grades and the general average weight.
    english = float(document.getElementById("english_grade").value)
    math = float(document.getElementById("math_grade").value)
    science = float(document.getElementById("science_grade").value)
    filipino = float(document.getElementById("filipino_grade").value)
    pe = float(document.getElementById("pe_grade").value)
    music = float(document.getElementById("music_grade").value)
    ict = float(document.getElementById("ict_grade").value)
    tle = float(document.getElementById("TLE_grade").value)
    ve = float(document.getElementById("ve_grade").value)
    history = float(document.getElementById("history_grade").value)
    philo = float(document.getElementById("philo_grade").value)
    LT = float(document.getElementById("LT_grade").value)

    units = [5,4,3,2,1] #number of units for each subject
    #        0 1 2 3 4
    grades = (english, math, science, filipino, pe, music, ict, tle, LT, philo) #grades for each subject

    total_weighted_score = ((english * units[0]) + (math * units[0]) + (science * units[0]) + (history * units[2]) + (filipino * units[2]) + (pe * units[4]) + 
                            (music * units[4]) + (ict * units[3]) + (tle * units[3]) + (ve * units[0]) + (LT * units[4]) + (philo * units[2]))

    total_units = sum(units[:len(grades)])  # sum only the units corresponding to the number of grades provided
    gwa = total_weighted_score / total_units

    display(f"GWA: {gwa:.2f}", target="output")

def summary(e): #This code shows the summary of all the exams
    summary = {"English": float(document.getElementById("english_grade").value),
               "Math": float(document.getElementById("math_grade").value),
               "Science": float(document.getElementById("science_grade").value),
               "Filipino": float(document.getElementById("filipino_grade").value),
               "PE": float(document.getElementById("pe_grade").value),
               "Music": float(document.getElementById("music_grade").value),
               "ICT": float(document.getElementById("ict_grade").value),
               "TLE": float(document.getElementById("TLE_grade").value),
               "VE" : float(document.getElementById("ve_grade").value),
               "History" : float(document.getElementById("history_grade").value),
               "Philo" : float(document.getElementById("philo_grade").value),
               "LT" : float(document.getElementById("LT_grade").value)
               }

    display(f"English : {summary["English"]}", target="summary")
    display(f"Math : {summary["Math"]}", target="summary")
    display(f"Filipino : {summary["Filipino"]}", target="summary")
    display(f"History : {summary["History"]}", target="summary")
    display(f"Philo : {summary["Philo"]}", target="summary")
    display(f"VE : {summary["VE"]}", target="summary")
    display(f"Music : {summary["Music"]}", target="summary")
    display(f"ICT : {summary["ICT"]}", target="summary")
    display(f"LT/CAT : {summary["LT"]}", target="summary")
    display(f"PE : {summary["PE"]}", target="summary")
