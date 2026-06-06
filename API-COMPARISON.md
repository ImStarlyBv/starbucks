# Starbucks API vs NutriBucks — Product Comparison

> Fetched live from `starbucks.com/apiproxy/v1/ordering/menu` on 2026-06-06.

## At a glance

| | Count |
|---|---|
| Live Starbucks menu (API) | **244** |
| Our `nutrition_full.json` | **391** |
| Exact name match (in both) | **147** |
| Only in API — new or renamed, missing from our data | **97** |
| Only in nutrition — gone from Starbucks menu | **244** |
| Same product, name slightly changed | **5** |

---

## Products only in API — not in our data (97)

These are **on the live Starbucks menu but missing from `nutrition_full.json`**.
The nutrition data needs updating to include these.

- All In™ Madagascar Vanilla, Honey & Almonds Bar
- Banana, Walnut & Pecan Loaf
- Blonde Roast - Starbucks® Sunsera
- Butterfly Energy Drink
- Caffè Verona®
- Cannon Ball Drink
- Cannon Ball Energy Drink
- Caramel Frappuccino® Blended Beverage
- Caramel Ribbon Crunch Frappuccino® Blended Beverage
- Chamomile Mint Blossom Tea
- Coffee Frappuccino® Blended Beverage
- Coffee Traveler – Decaf Pike Place® Roast
- Coffee Traveler – Pike Place® Roast
- Cold Brew
- Country Archer™ – Hickory Smoke Turkey Jerky
- DASANI® Water
- Decaf Pike Place Roast
- Decaf Roast - Pike Place® Roast
- Decaf Sumatra
- Dragon Drink®
- Dragon Energy Drink
- Ellenos Muesli Yogurt
- Ellenos Strawberry Shortcake Greek Yogurt
- Ellenos® Muesli Yogurt – No Added Sugar
- Emperor's Clouds & Mist® Tea
- Espresso Roast
- Ethos® Water
- Evolution Fresh® Pure Orange
- Featured Dark Roast - Starbucks 1971 Roast™
- Guatemala Antigua
- Horchata Crème Frappuccino® Blended Beverage
- Horchata Frappuccino® Blended Beverage
- Horizon Organic® Lowfat Chocolate Milk
- Horizon Organic® Lowfat Milk
- Iced Horchata Shaken Espresso
- Iced Ube Coconut Cream Shaken Espresso
- Italian Roast
- Khloud™ Sweet & Salty Kettle Corn Protein Popcorn
- Khloud™ White Cheddar Protein Popcorn
- Koia® Cacao Bean Nutrition Shake
- Koia® Vanilla Bean Nutrition Shake
- Komodo Dragon Blend®
- Lavender Crème Frappuccino® Blended Beverage
- MUSH Chocolate Peanut Butter Protein Overnight Oats
- Mango Dragonfruit Energy Refresher
- Mango Dragonfruit Lemonade Energy Refresher
- Mango Dragonfruit Lemonade Refresher
- Mango Dragonfruit Refresher
- Mango Dream
- Mango Strawberry Lemonade Refresher
- Mango Strawberry Refresher
- Matcha Crème Frappuccino® Blended Beverage
- Medium Roast - Pike Place® Roast
- Mint Majesty® Tea
- Mocha Cookie Crumble Frappuccino® Blended Beverage
- Mocha Frappuccino® Blended Beverage
- Organic Valley Stringles® Mozzarella String Cheese
- Organic Yukon Blend®
- Perfect Bar® – Dark Chocolate Chip Peanut Butter
- Pike Place® Roast
- Pink Cannon Ball Drink
- Pink Cannon Ball Energy Drink
- Pink Drink
- Pink Energy Drink
- Pistachio Crème Frappuccino® Blended Beverage
- Pistachio Frappuccino® Blended Beverage
- Poppi® Grape Soda
- Poppi® Shirley Temple Soda
- SkinnyDipped Coconut Almond Bite
- Small Shopping Bag
- Sol-ti® GINGER SuperShot®
- Sol-ti® TURMERIC SuperShot®
- Spindrift® Lemon Sparkling Water
- Starbucks 1971 Roast™
- Starbucks Siren’s Blend™
- Starbucks VIA® Instant Decaf Italian Roast
- Starbucks VIA® Instant Sweetened Iced Coffee
- Starbucks® Blonde Espresso Roast
- Starbucks® Green Apron Blend™
- Starbucks® Iced Energy Blueberry Lemonade
- Starbucks® Iced Energy Tropical Peach
- Starbucks® Sun-Dried Ethiopia Highlands
- Starbucks® Sunsera Blend
- Strawberry Açaí Energy Refresher
- Strawberry Açaí Lemonade Energy Refresher
- Strawberry Açaí Lemonade Refresher
- Strawberry Açaí Refresher
- Strawberry Crème Frappuccino® Blended Beverage
- Strawberry Matcha Loaf​
- Sumatra
- That's It® – Apple + Blueberry Bar
- That's It® – Apple + Mango Bar
- Tree Top® Organic Apple Juice – 6.75 fl oz
- Tropical Butterfly Lemonade Energy Refresher
- Vanilla Bean Crème Frappuccino® Blended Beverage
- Veranda Blend®
- Waiākea Hawaiian Volcanic Water

---

## Name changes — same product, different string (5)

These exist in both but with punctuation/spelling differences.
Images are already copied under both names in `images/`.

| nutrition_full.json | Live API name |
|---|---|
| Strawberry Matcha Loaf | Strawberry Matcha Loaf​ |
| Banana Walnut & Pecan Loaf | Banana, Walnut & Pecan Loaf |
| Perfect Bar® - Dark Chocolate Chip Peanut Butter | Perfect Bar® – Dark Chocolate Chip Peanut Butter |
| That's It® - Apple + Mango Bar | That's It® – Apple + Mango Bar |
| That's It® - Apple + Blueberry Bar | That's It® – Apple + Blueberry Bar |

---

## Gone from Starbucks menu — only in our data (244)

These are in `nutrition_full.json` but **not on the live Starbucks menu**.
Safe to exclude from the site.

### Hot (53)

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
- Matcha Latte
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

### Cold (101)

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
- Iced Caffè Americano
- Iced Caffè Latte
- Iced Caffè Mocha
- Iced Caramel Apple Cream Latte
- Iced Caramel Brulée Latte
- Iced Caramel Macchiato
- Iced Chai Latte
- Iced Chai Tea Latte with Oleato Golden Foam™
- Iced Cherry Chai Latte
- Iced Chestnut Praline Latte
- Iced Chocolatey Mousse Latte
- Iced Cinnamon Dolce Latte
- Iced Coffee Clover Vertica™
- Iced Coffee with Milk
- Iced Eggnog Latte
- Iced Espresso
- Iced Flat White
- Iced Gingerbread Chai
- Iced Gingerbread Cream Matcha Latte
- Iced Gingerbread Latte
- Iced Gingerbread Oatmilk Chai
- Iced Honey Almondmilk Flat White
- Iced Honey Apple Almondmilk Flat White
- Iced Horchata Oatmilk Shaken Espresso
- Iced London Fog Latte
- Iced Matcha Lemonade
- Iced Matcha Tea Latte with Oleato Golden Foam™
- Iced Nondairy Salted Caramel Cookie Matcha
- Iced Pecan Crunch Oatmilk Latte
- Iced Peppermint Mocha
- Iced Peppermint White Chocolate Mocha
- Iced Pistachio Latte
- Iced Pumpkin Cream Chai Latte
- Iced Pumpkin Spice Latte
- Iced Royal English Breakfast Tea Latte
- Iced Starbucks® Blonde Vanilla Latte
- Iced Sugar Cookie Almondmilk Latte
- Iced Sugar Cookie Breve
- Iced Sugar Cookie Cream Matcha Latte
- Iced Sugar Cookie Latte
- Iced Toffee Nut Cream Matcha Latte
- Iced Toffee Nut Latte
- Iced Vanilla Cream Protein Latte
- Iced White Chocolate Mocha
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

### Bakery (22)

- Baked Apple Croissant
- Banana Walnut & Pecan Loaf
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
- Strawberry Matcha Loaf
- Sugar Plum Cheese Danish
- Turkey Sage Danish
- Valentine Cake Pop
- Vanilla Bean Custard Danish

### Snacks & Sweets (14)

- Country Archer - Hickory Smoked Turkey Jerkey
- Dark Chocolate Covered Espresso Beans
- Dark Chocolate Peanut Butter Cups
- KIND Peanut Butter Dark Chocolate Bar
- Perfect Bar® - Dark Chocolate Chip Peanut Butter
- Perfectly Salted Chips
- Rip van Wafels – Honey & Oats
- Salted Almond Chocolate Bites
- Shortbread Cookies
- Siete Lime Grain Free Tortilla Chips
- Starbucks Butter Popcorn
- String Cheese
- That's It® - Apple + Blueberry Bar
- That's It® - Apple + Mango Bar
