# Steam-Retriever-Alpha-v0.1
This is a very simple python console program written to retrieve data about a specific steam market item (every five minutes). It will be developed more in the future adding more advanced features. Possibly it will be converted into a library.

**USAGE :**

When you look at the text, you will see some lines of code between two fancy comment lines, they are supposed to be the configuration to this program, i'll break it down step by step.


    ############## CONFIG ###############
    
    item_appid = '264710'							
    item_currency = '1'
    item_hash_name = 'Planet%204546B%20Postcard'
    
    #####################################

The first line of configuration is about the `app_id` :

    item_appid = '264710'
This app-id is for the game called Subnautica on Steam , you can easily find app ids by a simple Google search. Remember to enclose it in quotation marks.

Then the second line is for the `currency` to retrieve the price in , and here you need to write the currency id . Here '1' is for US Dollar (USD) 

    item_currency = '1'


Finally , the `item_hash_name` , it can be easily found from the item's listing page's URL.

![](https://i.imgur.com/vbhZS9l.png)

**That is it, save the file , and run the program.**
