from pyscript import document, display

def general_weighted_average(e):

    # Get student info
    fname = document.getElementById('fname').value
    sname = document.getElementById('sname').value
    g_s = document.getElementById('g_s').value

    # Get grades
    math = float(document.getElementById('math').value)
    filipino = float(document.getElementById('filipino').value)
    science = float(document.getElementById('science').value)
    ict = float(document.getElementById('ict').value)
    music_arts = float(document.getElementById('m_a').value)
    social_studies = float(document.getElementById('ss').value)

    # Weighted calculation
    weighted_sum = (
        (math * 5) +
        (filipino * 3) +
        (science * 5) +
        (ict * 2) +
        (music_arts * 1) +
        (social_studies * 3)
    )
    total_units = 5 + 3 + 5 + 2 + 1 + 3
    gwa = weighted_sum / total_units

    # get input values (as before)
    subjects = ["Mathematics", "Filipino", "Science", "ICT", "Music & Arts", "Social Studies"]

    summary_text =  f"""
    {subjects[0]}:{math:.0f}
    {subjects[1]}:{filipino:.0f}
    {subjects[2]}:{science:.0f}
    {subjects[3]}:{ict:.0f}
    {subjects[4]}:{music_arts:.0f}
    {subjects[5]}:{social_studies:.0f}
    """

    # Show results
    display(f'Name: {fname} {sname} — {g_s}', target="student_info")
    display(summary_text, target="summary")
    display(f'Your General Weighted Average is {gwa:.2f}', target="output")