# Products Without Images — Exclude from NutriBucks

Cross-checked against the **live Starbucks menu API** on 2026-06-06.

## Summary

| Status | Count |
|---|---|
| ✅ Images downloaded | 257 |
| ✅ Punctuation-mismatch fixed (image copied) | 5 |
| ⚠️ On live menu but Starbucks CDN image is broken | 3 |
| ❌ Confirmed NOT on live Starbucks menu | 226 |

---

## ⚠️ On the menu — CDN image broken

These 3 products **are** on the current Starbucks menu but their images return 403
even on starbucks.com itself (data bug in Starbucks' own API). Exclude or use a
placeholder until Starbucks fixes it.

- **Vanilla Crème** (Hot)
- **Iced Caffè Mocha** (Cold)
- **Blended Strawberry Lemonade** (Cold)

---

## ❌ Confirmed gone from the live menu (226 products)

These products exist in `nutrition_full.json` but are **not on the current Starbucks menu**.
Safe to exclude from your site.

### Hot (52)

- Americano Misto
- Apple Crisp Oatmilk Macchiato
- Blonde Roast - Sunsera
- Blonde Roast - Veranda Blend®
- Brown Sugar Oat Americano
- Caffè Verona® Clover Vertica™
- Caramel Apple Spice
- Caramel Brulée Crème
- Caramel Brulée Latte
- Chai Tea
- Chamomile Mint Blossom
- Chestnut Praline Crème
- Chestnut Praline Latte
- Chocolatey Mousse Latte
- Clover Vertica Christmas Blend
- Clover® Malawi Sable Farms Starbucks Reserve®
- Clover® Starbucks Reserve® Vietnam Da Lat
- Eggnog Latte
- Emperor’s Clouds & Mist®
- Featured Dark Roast
- Featured Dark Roast Caffè Verona®
- Featured Decaf Roast Decaf Pike Place® Roast
- Featured Medium Roast Pike Place® Roast
- Gingerbread Chai
- Gingerbread Latte
- Gingerbread Matcha Latte
- Gingerbread Oatmilk Chai
- Honey Almondmilk Flat White
- Jade Citrus Mint® Brewed Tea
- Medium Roast - Guatemala Casi Cielo®
- Mint Majesty®
- Pecan Crunch Oatmilk Latte
- Pecan Oatmilk Cortado
- Peppermint Hot Chocolate
- Peppermint Mocha
- Peppermint White Chocolate Mocha
- Peppermint White Hot Chocolate
- Pumpkin Spice Crème
- Pumpkin Spice Latte
- Royal English Breakfast Tea Latte
- Single-Origin Ethiopia
- Starbucks Reserve® Christmas 2023 Clover®
- Starbucks Reserve® Christmas 2024 Clover Vertica
- Starbucks® Christmas Blonde Roast Clover Vertica™ Brewed Coffee
- Steamed Apple Juice
- Sugar Cookie Almondmilk Latte
- Sugar Cookie Breve
- Sugar Cookie Latte
- Toffee Nut Latte
- Toffee Nut Matcha Latte
- Veranda Blend® Clover Vertica™
- White Hot Chocolate

### Cold (89)

- Blackberry Sage Lemonade Refresher
- Blackberry Sage Refresher
- Brew DR. Island Mango Kombucha
- Brew DR. Superberry Kombucha
- Chocolate Cream Protein Cold Brew
- Chocolate Hazelnut Cookie Cold Brew
- Cinnamon Caramel Cream Cold Brew
- Cinnamon Caramel Cream Nitro Cold Brew
- Cran-Merry Drink
- Cran-Merry Orange Lemonade Refresher
- Cran-Merry Orange Refresher
- Dragon Drink® Starbucks Refreshers® Beverage
- Dragon Drink® Starbucks Refreshers® Beverage with Oleato Golden Foam™
- Elphaba’s Cold Brew
- Evolution Fresh® Orange
- Frozen Mango Dragonfruit Lemonade Starbucks Refreshers® Beverage
- Frozen Pineapple Passionfruit Lemonade Starbucks Refreshers® Beverage
- Frozen Strawberry Açaí Lemonade Starbucks Refreshers® Beverage
- Frozen Tropical Citrus Iced Energy with Strawberry Puree
- Glinda’s Pink Potion
- Iced Apple Crisp Nondairy Cream Chai
- Iced Apple Crisp Oatmilk Macchiato
- Iced Apple Crisp Oatmilk Shaken Espresso
- Iced Banana Cream Protein Matcha
- Iced Brown Sugar Cream Protein Matcha
- Iced Caramel Apple Cream Latte
- Iced Caramel Brulée Latte
- Iced Chai Tea Latte with Oleato Golden Foam™
- Iced Cherry Chai Latte
- Iced Chestnut Praline Latte
- Iced Chocolatey Mousse Latte
- Iced Coffee Clover Vertica™
- Iced Coffee with Milk
- Iced Eggnog Latte
- Iced Gingerbread Chai
- Iced Gingerbread Cream Matcha Latte
- Iced Gingerbread Latte
- Iced Gingerbread Oatmilk Chai
- Iced Honey Almondmilk Flat White
- Iced Honey Apple Almondmilk Flat White
- Iced Horchata Oatmilk Shaken Espresso
- Iced Matcha Lemonade
- Iced Matcha Tea Latte with Oleato Golden Foam™
- Iced Nondairy Salted Caramel Cookie Matcha
- Iced Pecan Crunch Oatmilk Latte
- Iced Peppermint Mocha
- Iced Peppermint White Chocolate Mocha
- Iced Pumpkin Cream Chai Latte
- Iced Pumpkin Spice Latte
- Iced Royal English Breakfast Tea Latte
- Iced Sugar Cookie Almondmilk Latte
- Iced Sugar Cookie Breve
- Iced Sugar Cookie Cream Matcha Latte
- Iced Sugar Cookie Latte
- Iced Toffee Nut Cream Matcha Latte
- Iced Toffee Nut Latte
- Iced Vanilla Cream Protein Latte
- Koia® Cacao Bean Protein Shake
- Koia® Vanilla Bean Protein Shake
- Mango Dragonfruit Starbucks Refreshers® Beverage
- Melon Burst Iced Energy
- Midnight Drink
- Oleato Golden Foam™ Cold Brew
- Oleato™ Caffé Latte with Oatmilk
- Oleato™ Gingerbread Oatmilk Latte
- Oleato™ Iced Shaken Espresso with Oatmilk and Toffeenut
- Paradise Drink Starbucks Refreshers® Beverage
- Paradise Drink Starbucks Refreshers® Beverage with Oleato Golden Foam™
- Pineapple Passionfruit Lemonade Starbucks Refreshers® Beverage
- Pineapple Passionfruit Starbucks Refreshers® Beverage
- Pink Drink Starbucks Refreshers® Beverage
- Pumpkin Cream Cold Brew
- Raspberry Cream Cold Brew
- Salted Pecan Crunch Cold Brew
- Spindrift® Grapefruit Sparkling Water
- Starbucks Reserve® Cold Brew
- Starbucks® Cold Brew Coffee
- Starbucks® Cold Brew Coffee with Milk
- Starbucks™ Baya Energy Mango Guava
- Starbucks™ Baya Energy Raspberry Lime
- Strawberry Açaí Starbucks Refreshers® Beverage
- Summer Skies Drink
- Summer-Berry Lemonade Refresher
- Summer-Berry Refresher
- Teavana® Mango Black Tea
- Teavana® Sparkling Unsweetened Peach Nectarine Green Tea
- Tree Top Apple Juice Box
- Tropical Citrus Iced Energy
- White Chocolate Strawberry Cream Cold Brew

### Frappe (45)

- Apple Crisp Oatmilk Crème Frappuccino®
- Apple Crisp Oatmilk Frappuccino®
- Brown Sugar Strato™ Frappuccino®
- Caffè Vanilla Frappuccino®
- Caramel Brulée Crème Frappuccino®
- Caramel Brulée Frappuccino®
- Caramel Frappuccino®
- Caramel Ribbon Crunch Crème Frappuccino®
- Caramel Ribbon Crunch Frappuccino®
- Chai Crème Frappuccino®
- Chestnut Praline Crème Frappuccino®
- Chestnut Praline Frappuccino®
- Chocolate Cookie Crumble Crème Frappuccino®
- Chocolate-Covered Strawberry Crème Frappuccino®
- Coffee Frappuccino®
- Double Chocolaty Chip Crème Frappuccino®
- Espresso Frappuccino®
- Gingerbread Cream Frappuccino®
- Gingerbread Frappuccino®
- Horchata Crème Frappuccino®
- Horchata Frappuccino®
- Java Chip Frappuccino®
- Lavender Crème Frappuccino®
- Matcha Crème Frappuccino®
- Mocha Cookie Crumble Frappuccino®
- Mocha Frappuccino®
- Peppermint Mocha Crème Frappuccino®
- Peppermint Mocha Frappuccino®
- Peppermint White Chocolate Crème Frappuccino®
- Peppermint White Chocolate Mocha Frappuccino®
- Pistachio Crème Frappuccino®
- Pistachio Frappuccino®
- Pumpkin Spice Crème Frappuccino®
- Pumpkin Spice Frappuccino®
- Salted Caramel Mocha Strato™ Frappuccino®
- Strawberry Crème Frappuccino®
- Strawberry Matcha Strato™ Frappuccino®
- Strawberry Shortcake Frappuccino®
- Sugar Cookie Almondmilk Crème Frappuccino®
- Sugar Cookie Almondmilk Frappuccino®
- Toffee Nut Cream Frappuccino®
- Toffee Nut Frappuccino®
- Vanilla Bean Crème Frappuccino®
- White Chocolate Crème Frappuccino®
- White Chocolate Mocha Frappuccino®

### Food/Meal (9)

- Berry Trio Parfait
- Cheddar & Uncured Salami Protein Box
- Chicken, Maple Butter & Egg Sandwich
- Chipotle Almond Dip by Bitchin’ Sauce®
- Eggs & Gouda Protein Box
- Italian Sausage Egg Bites
- Kale & Mushroom Egg Bites
- PB&J Protein Box
- Turkey, Provolone & Pesto on Ciabatta

### Bakery (20)

- Baked Apple Croissant
- Blueberry Muffin
- Blueberry Scone
- Bullseye Cookie
- Cookies & Cream Cake Pop
- Cranberry Bliss® Bar
- Cranberry Bliss® Bar Tray
- Dark Toffee Bundt
- Gingerbread Loaf
- Glazed Doughnut
- Penguin Cookie
- Peppermint Brownie Cake Pop
- Polar Bear Cake Pop
- Pumpkin Cream Cheese Muffin
- Snowman Cake Pop
- Snowman Cookie
- Sugar Plum Cheese Danish
- Turkey Sage Danish
- Valentine Cake Pop
- Vanilla Bean Custard Danish

### Snacks & Sweets (11)

- Country Archer - Hickory Smoked Turkey Jerkey
- Dark Chocolate Covered Espresso Beans
- Dark Chocolate Peanut Butter Cups
- KIND Peanut Butter Dark Chocolate Bar
- Perfectly Salted Chips
- Rip van Wafels – Honey & Oats
- Salted Almond Chocolate Bites
- Shortbread Cookies
- Siete Lime Grain Free Tortilla Chips
- Starbucks Butter Popcorn
- String Cheese
