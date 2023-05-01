#Ruslan Gusakov
network_req={'CSC 110', 'ETR 164', 'ITN 101',}

network_elect = {'CSC 201', 'CSC 202', 'CSC 205', 'ETR 113', 'ETR 290', 'ITN 106' , 'ITN 120', 'ITN 151', 'ITN 170', 'ITN 260', 'ITN 290', 'ITP 120', 'ITP 132', 'ITP 200', 'ITP 220', 'ITP 290', 'MTH 131', 'MTH 161', 'MTH 162', 'MTH 263',}

info_req = { 'CSC110', 'ENG 111', 'ENG 112', 'ETR 149', 'ETR 164', 'ITD 110', 'ITD 132', 'ITE 182', 'ITE 215', 'ITN 101', 'ITN 106', 'ITN 111', 'ITP 120', 'MTH 131',}

info_elect = {'ITN 170', 'ITN 208', 'ITN 260', 'ITN 261', 'ITN 276', 'ITN 277', 'ITP 132', 'ITP 136', 'ITP 150', 'ITP 220',}

dash_line = "--------------------------------------------------"

def main ():
    print("n********PIEDMONT VIRGINIA COMMUNITY COLLEGE********")
    process_network_courses ()
    display_network,courses ()

    process_info_courses ()
    display_info_courses ()

    process_courses_in_both ()

def process_network_courses ():
    global network_elect
    global num_net_req, num_net_elect, tot_net, all_net_courses
    temp_set= set()

    for course in network_elect:
        asterisk_course="*"+course
        temp_set.add(asterisk_course)
        
    network_elect.clear()
    network_elect=temp_set.copy()

    num_net_req = len(network_req)
    num_net_elect = len(network_elect)
    tot_net= num_net_req + num_net_elect
    all_net_courses = network_req.union(network_elect)
def display_network_courses ():
    print ("\nCERTIFICATE: Computer & Network Support Technologies")
    print (dash_line)
    print ("Number of required courses   :" +str(num_net_req))
    print ("Number of elective courses   :" +str(num_net_elect))
    print ("Total number of Cert. courses:" +str(tot_net))
    print (dash_line)
    print ("All Certificate courses:  ")
    num =1
    for course in all_net_courses:
        print (course, end = " ")
        num += 1
        if num % 5 == 0:
            print ()
    print ("\nNOTES:")
    print ("  *Asterisk indicates ELECTIVE course")
    print ("  Students choose 3 technical elective courses")
    print (dash_line)

def process_info_courses ():

    print("here")

def display_info_courses ():

    print("now here")

def process_courses_in_both ():
    both_req= network_req.intersection(info_req)
    print (dash_line)
    print ("REQUIRED courses in both programs:")
    num = 1
    for course in both_req:
        print(course, end = " ")
        num +=1
        if num % 5 == 0:
            print ()

main()



dash_line = "\n-------------------------------------------------"
filename= "pvcc.txt"
global out

def main () :
    global out
    out = open(filename, "w")
    out.write ("\n********PIEDMONT VIGINIA COMMUNITY COLLEGE*******")
    process_network_courses ()
    display_network_courses ()

    process_info_courses()
    display_info_courses ()

    process_courses_in_both ()
    out.close ()
    print("To see results open file: "+ filename)

def display_network_courses():
    global out
    out.write ("\nCERTIFICATE: Computer & Network Support Technologies")
    out.write (dash_line)
    out.write ("\nNumber of required courses    : " + str(num_net_req))
    out.write ("\nNumber of elective courses    : " + str(num_net_elect))
    out.write ("\nTotal number of Cert. courses : " + str(tot_net))
    out.write (dash_line)
    out.write ("\nAll Certificate courses: ")
    num=1
    for course in all_net_courses:
        out.write(course + "   ")
        num += 1
        if num % 5 == 0:
            out.write("\n")
    out.write ("\nNOTES:")
    out.write ("\n   *Asterisk indicates ELECTIVE course")
    out.write ("\n   Students choose 3 technical elective courses")
    out.write (dash_line)