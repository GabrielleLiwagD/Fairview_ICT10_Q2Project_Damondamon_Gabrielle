from pyscript import display, document


def student_info(e):
    last_name = str(document.getElementById("last_name").value)
    first_name = str(document.getElementById("first_name").value)
    
    display(f"Student Name: {last_name}, {first_name}", target = "student_info")

def calculate_gwa(e):
    english = float(document.getElementById("english_grade").value)
    math = float(document.getElementById("math_grade").value)
    science = float(document.getElementById("science_grade").value)
    filipino = float(document.getElementById("filipino_grade").value)
    pe = float(document.getElementById("pe_grade").value)
    music = float(document.getElementById("music_grade").value)
    ict = float(document.getElementById("ict_grade").value)
    tle = float(document.getElementById("TLE_grade").value)
    

    units = [5,4,3,2,1] #number of units for each subject
    grades = [english, math, science, filipino, pe, music, ict, tle] #grades for each subject

    total_weighted_score = (english * units[0] + math * units[0] + science * units[0] +
                            filipino * units[3] + pe * units[1] + music * units[1] + ict * units[2] + tle * units[3])

    total_units = sum(units[:len(grades)])  # sum only the units corresponding to the number of grades provided
    gwa = total_weighted_score / total_units

    display(f"GWA: {gwa:.2f}", target="output")

def summary(e):
    summary = {"English": float(document.getElementById("english_grade").value),
               "Math": float(document.getElementById("math_grade").value),
               "Science": float(document.getElementById("science_grade").value),
               "Filipino": float(document.getElementById("filipino_grade").value),
               "PE": float(document.getElementById("pe_grade").value),
               "Music": float(document.getElementById("music_grade").value),
               "ICT": float(document.getElementById("ict_grade").value),
               "TLE": float(document.getElementById("TLE_grade").value)
               }

    display(f"Summary of Grades: {summary['English']}", target="summary")
    display(f"Summary of Grades: {summary['Math']}", target="summary")
    display(f"Summary of Grades: {summary['Science']}", target="summary")
    display(f"Summary of Grades: {summary['Filipino']}", target="summary")
    display(f"Summary of Grades: {summary['PE']}", target="summary")
    display(f"Summary of Grades: {summary['Music']}", target="summary")
    display(f"Summary of Grades: {summary['ICT']}", target="summary")
    display(f"Summary of Grades: {summary['TLE']}", target="summary")