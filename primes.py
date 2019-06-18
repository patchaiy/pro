def check(string) : 
  
    # set function convert string 
    # into set of characters . 
    p = set(string) 
  
    # declare set of '0', '1' . 
    s = {'0', '1'} 
  
   
    if s == p or p == {'0'} or p == {'1'}: 
        print("yes") 
    else : 
        print("no") 
  
  
          
# driver code 
if __name__ == "__main__" : 
  
    string = input()
  
    # function calling 
    check(string) 
