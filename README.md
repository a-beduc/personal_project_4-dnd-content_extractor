2024-07-27 : What i want to do : 
- extract content from the website https://www.thievesguild.cc/equipment/ 
- translate the content
- add my own personal content
- put everything in a local database

Classes to create (TO-DO LIST):
- ShopScraper (Collect content of a single shop)
- Item (An item with its attributes)
- Shop (Every item of a shop)
- ItemManager (Centralise every shop and delete duplicates)
- CSVExporter (Extract every items in a single table to translate the content)
- DatabaseManager (Use CSV files and create a database)

2024/08/02 Notes :

Table items :
ID
Name (eng) [key]
Name (fr)
Description
Category
Sub-Category
Price
Weight

Table Shop x :
Name (eng) [key]
Urban
Rural
Stock