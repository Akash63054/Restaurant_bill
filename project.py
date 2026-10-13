menu_items = ["Burger", "Pizza", "Pasta", "Fries", "Coke"]
menu_prices = [120, 250, 180, 90, 50]
total = 0  
gst = 18 
user_items = []
user_prices = []
while True:
    print("Menu items : ")
    for i in range(len(menu_items)):
        print(f"{i+1} {menu_items[i]}: {menu_prices[i]}")
    print("Enter 'Done' to stop : ")
    user_item = input("Enter Your Item : ")
    if user_item == "done" or user_items == "DONE":
            gst_cost = total*gst/100
            total_with_gst = total + gst_cost
            coupon = input("Enter Your Coupon : ")
            print("="*10,"Delious Restaurant","="*10)
            print(f"Your orders items and price : ")
            for i in range(len(user_items)):
                print(f"{i+1} {user_items[i]}:{user_prices[i]}")
            print("="*20)
            print(f"Total Bill : {total}")
            print(f"18 % gst : {gst_cost}")
            if coupon == "WELCOME50" or coupon == "welcome50":
                coupon_offer = total_with_gst - 50
                print(f"Your Total Bill After Coupon offer : {coupon_offer}")
            elif coupon == "SAVE10" or coupon == "save10":
                 coupon_offer = total_with_gst * 10/100
                 total_with_coupon = int(total_with_gst - coupon_offer)
                 print(f"Your Total Bill After coupon offer : {total_with_coupon}")
            
            else :
                 print(f"Total Bill With Gst : {total_with_gst}")
            print("-"*10,"Thank You","-"*10 )
            
            break
    if user_item in menu_items: 
        i = menu_items.index(user_item)
        price = menu_prices[i]
        user_items.append(user_item)
        user_prices.append(price) 
        total += price
        print(f"{user_item} added : {price}")
    else:
        print("Item not available in the menu!")
            
            
    
       
    
            
    
       
    