def main():
  plate_list = []
  go_again = 'y'
  while go_again != 'n':
    while True:
        Make_list = ["Rambler", "Renault", "Peugeot", "Rover", "Ford", "Dealer"]
        print Make_list
        pick_make = "Wally"
        pick_make = raw_input("Car Make?")
        print pick_make
        print go_again
        if pick_make == "Rambler":
            Rambler_list = ["Gremlin", "Hornet", "Matador", "Rebel", "Classic", "Ambassador", "Javelin", "American",
                            "AMX"]
            print Rambler_list
            pick_model = raw_input("please enter Rambler model: ")
            if pick_model == "h":
                Rambler_list = ["Hornet"]
            elif pick_model == "m":
                Rambler_list = ["Matador"]
            elif pick_model == "r":
                Rambler_list = ["Rebel", "NSW"]
            elif pick_model == "rm":
                Rambler_list = ["Rebel", "Matador", "NSW2"]
            elif pick_model == "rac":
                Rambler_list = ["Rebel", "American","Classic"]
            elif pick_model == "rmh":
                Rambler_list = ["Rebel", "Matador", "Hornet"]
            elif pick_model == "j":
                Rambler_list = ["Javelin"]
            elif pick_model == "c":
                Rambler_list = ["Classic"]
            elif pick_model == "an":
                Rambler_list = ["American"]
            elif pick_model == "x":
                Rambler_list = ["AMX"]
            elif pick_model == "ar":
                Rambler_list = ["Ambassador"]
            else:
                Rambler_list = ["Gremlin", "Hornet", "Matador", "Rebel", "Classic", "Ambassador", "Javelin", "American", "AMX"]
         #   ads_table = get_sql_data(car_model_list=Rambler_list, car_make="Rambler", connectstring="advertisements_indexed.db",
          #                           jurisdiction="NSW")
            break
        elif pick_make == "Ford":
            Ford_list = ["Falcon", "Cortina", "Capri"]
  #          ads_table = get_sql_data(car_model_list=Ford_list, car_make="Ford", connectstring="advertisements_indexed.db",
   #                                  jurisdiction="NSW")
            break
        elif pick_make == "Renault":
            Renault_list = ["R8", "R10", "R12", "R16", "R10S", "10S", "R17", "RXX"]
            print Renault_list
            pick_model = raw_input("please enter Renault model: ")
            if pick_model != "all":
                Renault_list = [pick_model]
 #           ads_table = get_sql_data(car_model_list=Renault_list, car_make ="Renault", connectstring="advertisements_indexed.db",
    #                               jurisdiction="NSW")
            break
        elif pick_make == "Peugeot":
            Peugeot_list = ["403", "403B", "404", "504"]
            print Peugeot_list
            pick_model = raw_input("please enter Peugeot model: ")
            if pick_model != "all":
                Peugeot_list = [pick_model]
#            ads_table = get_sql_data(car_model_list=Peugeot_list, car_make ="Peugeot", connectstring="advertisements_indexed.db",
     #                              jurisdiction="NSW")
            break
        elif pick_make == "Rover":
            Rover_list = ["2000", "2000TC", "3500", "P5B", "P5", "P5Bcoupe", "P5coupe", "100"]
            print Rover_list
            pick_model = raw_input("please enter Rover model: ")
            if pick_model != "all":
                Rover_list = [pick_model]
#            ads_table = get_sql_data(car_model_list=Rover_list, car_make ="Rover", connectstring="advertisements_indexed.db",
      #                             jurisdiction="NSW")
            break
        elif pick_make == "mm":
            print "ouch == mm"
            pick_model = raw_input("please enter model: ")
            if pick_model == "h":
                Rambler_list = ["Hornet"]
            elif pick_model == "m":
                Rambler_list = ["Matador"]
            elif pick_model == "r":
                Rambler_list = ["Rebel"]
            elif pick_model == "rm":
                Rambler_list = ["Rebel", "Matador"]
            elif pick_model == "rac":
                Rambler_list = ["Rebel", "American","Classic"]
            elif pick_model == "rmh":
                Rambler_list = ["Rebel", "Matador", "Hornet"]
            elif pick_model == "j":
                Rambler_list = ["Javelin"]
            elif pick_model == "c":
                Rambler_list = ["Classic"]
            elif pick_model == "an":
                Rambler_list = ["American"]
            elif pick_model == "x":
                Rambler_list = ["AMX"]
            elif pick_model == "ar":
                Rambler_list = ["Ambassador", "NSW"]
            else:
                Rambler_list = ["Hornet", "Matador", "Rebel", "Classic", "Ambassador", "Javelin", "American", "AMX"]

 #           Mascot_list = ["Hornet", "Matador", "Rebel", "Classic", "Ambassador", "Javelin", "American", "AMX"]
       #     ads_table = get_sql_data_mascot(car_model_list=Rambler_list, car_make ="Rambler", connectstring="advertisements_indexed.db",
        #                             jurisdiction="NSW")
            break
        elif pick_make == 'x':
            print "ouch pick_make == x"
            break
        else:
            print "try again"
    print pick_make, "before goodbye"
    print "goodbye"

    go_again = raw_input("Go Again y/n: ")

  print "printing results"




if __name__ == '__main__':
    main()
