import matplotlib.pyplot as plt 
f= 50 # frequency =  50 hertz
number_of_poles = 8 
machine_constant = 0.5 # k 
synchronous_speed_Ns =  (120 *f)/ (number_of_poles)  
excitation_current = [ i for i in range(12) ]





def synchronous_generator():
    value = []
    for if_value in excitation_current:  
     if if_value <= 5:
      Emf_value  = machine_constant * if_value * synchronous_speed_Ns
      value.append(Emf_value)
     elif if_value <=10:
       Emf_value_2 = machine_constant * 5 * synchronous_speed_Ns + 15 * (if_value -0.5)
       value.append(Emf_value_2)
     else:
       new_Emf_value = 0.01 * if_value + Emf_value_2
       value.append(new_Emf_value)
    return value


print(synchronous_generator())
plt.plot(excitation_current,synchronous_generator())
plt.xlabel("Exciation current (if)")
plt.ylabel("Induced emf")
plt.title("OCC Curve of an Alternator")
plt.grid(True)
plt.show()



