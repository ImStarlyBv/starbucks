<!-- Extracted text from https://starbucks-calorie-calculator.com/starbucks-nutrition-calculator/ -->

Enable JavaScript and cookies to continue

<!-- NutriBucks - Home -->

<!DOCTYPE html>

<html class="light" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>NutriBucks | Your Healthier Coffee Journey</title>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Source+Sans+3:wght@400;600&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            "colors": {
                "outline": "#6f7a72",
                "on-error-container": "#93000a",
                "primary-container": "#006241",
                "background": "#e6fff6",
                "surface-container-low": "#dbfaf0",
                "on-secondary-fixed-variant": "#384a46",
                "on-secondary": "#ffffff",
                "surface-container-high": "#d0efe4",
                "tertiary-fixed": "#ffdad7",
                "surface-container": "#d6f5ea",
                "on-background": "#04201a",
                "on-tertiary-fixed": "#3d0608",
                "surface-container-highest": "#cbe9df",
                "surface-bright": "#e6fff6",
                "primary-fixed": "#a2f3c8",
                "secondary": "#4f625d",
                "on-secondary-fixed": "#0c1f1b",
                "surface-dim": "#c2e1d6",
                "outline-variant": "#bec9c0",
                "error-container": "#ffdad6",
                "surface": "#e6fff6",
                "on-surface": "#04201a",
                "on-secondary-container": "#556863",
                "inverse-primary": "#87d7ad",
                "on-tertiary-fixed-variant": "#76312f",
                "tertiary-container": "#883f3c",
                "on-primary-fixed": "#002113",
                "secondary-fixed": "#d2e7e0",
                "inverse-on-surface": "#d9f7ed",
                "surface-tint": "#146b4a",
                "on-tertiary": "#ffffff",
                "primary": "#00482f",
                "primary-fixed-dim": "#87d7ad",
                "tertiary": "#6b2927",
                "on-primary-container": "#8bdbb1",
                "on-primary-fixed-variant": "#005235",
                "tertiary-fixed-dim": "#ffb3ae",
                "on-surface-variant": "#3f4943",
                "on-tertiary-container": "#ffb9b4",
                "white": "#FFFFFF",
                "inverse-surface": "#1a352e",
                "error": "#ba1a1a",
                "surface-variant": "#cbe9df",
                "secondary-container": "#d2e7e0",
                "surface-container-lowest": "#ffffff",
                "secondary-fixed-dim": "#b6cbc4",
                "on-error": "#ffffff",
                "accent-cream": "#F2F0EB",
                "on-primary": "#ffffff",
                "warm-gray": "#808080",
                "success-green": "#00754A"
            },
            "borderRadius": {
                "DEFAULT": "0.25rem",
                "lg": "0.5rem",
                "xl": "0.75rem",
                "full": "9999px"
            },
            "spacing": {
                "margin-desktop": "40px",
                "gutter": "24px",
                "unit": "8px",
                "container-max": "1280px",
                "margin-mobile": "16px"
            },
            "fontFamily": {
                "headline-md": ["Plus Jakarta Sans"],
                "caption": ["Source Sans Three"],
                "label-md": ["Source Sans Three"],
                "display-lg": ["Plus Jakarta Sans"],
                "headline-lg": ["Plus Jakarta Sans"],
                "headline-lg-mobile": ["Plus Jakarta Sans"],
                "body-lg": ["Source Sans Three"],
                "body-md": ["Source Sans Three"]
            },
            "fontSize": {
                "headline-md": ["24px", {"lineHeight": "32px", "fontWeight": "600"}],
                "caption": ["12px", {"lineHeight": "16px", "fontWeight": "400"}],
                "label-md": ["14px", {"lineHeight": "20px", "letterSpacing": "0.01em", "fontWeight": "600"}],
                "display-lg": ["48px", {"lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                "headline-lg": ["32px", {"lineHeight": "40px", "fontWeight": "700"}],
                "headline-lg-mobile": ["28px", {"lineHeight": "36px", "fontWeight": "700"}],
                "body-lg": ["18px", {"lineHeight": "28px", "fontWeight": "400"}],
                "body-md": ["16px", {"lineHeight": "24px", "fontWeight": "400"}]
            }
          },
        },
      }
    </script>
<style>
        body {
            background-color: #e6fff6;
            scroll-behavior: smooth;
        }
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        .glass-card {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.3);
        }
        .search-shadow {
            box-shadow: 0 10px 30px -5px rgba(0, 72, 47, 0.1);
        }
    </style>
</head>
<body class="font-body-md text-on-surface">
<!-- TopAppBar -->
<header class="fixed top-0 w-full z-50 flex justify-between items-center px-margin-mobile md:px-margin-desktop h-16 bg-surface dark:bg-inverse-surface">
<div class="flex items-center gap-4">
<span class="font-headline-md text-headline-md font-bold text-primary-container dark:text-primary-fixed">NutriBucks</span>
</div>
<nav class="hidden md:flex items-center gap-8">
<a class="font-label-md text-label-md text-primary dark:text-primary-fixed font-bold hover:bg-surface-container-high transition-colors px-3 py-2 rounded-lg" href="#">Explore</a>
<a class="font-label-md text-label-md text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-high transition-colors px-3 py-2 rounded-lg" href="#">Calculator</a>
<a class="font-label-md text-label-md text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-high transition-colors px-3 py-2 rounded-lg" href="#">Favorites</a>
</nav>
<div class="flex items-center gap-4">
<button class="material-symbols-outlined text-primary p-2 hover:bg-surface-container-high rounded-full transition-all active:scale-95" data-icon="history">history</button>
<button class="material-symbols-outlined text-primary p-2 hover:bg-surface-container-high rounded-full transition-all active:scale-95" data-icon="favorite">favorite</button>
</div>
</header>
<main class="pt-24 pb-32">
<!-- Hero Section -->
<section class="max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop mb-16">
<div class="relative overflow-hidden rounded-[2rem] bg-primary-container p-8 md:p-16 flex flex-col items-center text-center">
<!-- Background Pattern -->
<div class="absolute inset-0 opacity-10 pointer-events-none" style="background-image: radial-gradient(circle at 2px 2px, white 1px, transparent 0); background-size: 32px 32px;"></div>
<h1 class="font-display-lg text-display-lg text-white mb-6 max-w-2xl">Fuel Your Day with Precision and Flavor</h1>
<p class="font-body-lg text-body-lg text-on-primary-container mb-10 max-w-xl">Master your nutrition without sacrificing your favorite brews. Calculate, customize, and conquer your health goals with NutriBucks.</p>
<!-- Search Bar -->
<div class="w-full max-w-2xl relative">
<div class="flex items-center bg-white rounded-full p-2 search-shadow">
<span class="material-symbols-outlined text-outline px-4" data-icon="search">search</span>
<input class="flex-1 bg-transparent border-none focus:ring-0 text-on-surface font-body-md py-3 px-2" placeholder="Search your favorite drink..." type="text"/>
<button class="bg-primary hover:bg-success-green text-white px-8 py-3 rounded-full font-label-md transition-all active:scale-95">Search</button>
</div>
</div>
</div>
</section>
<!-- Category Filters -->
<section class="max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop mb-12">
<div class="flex flex-wrap items-center justify-center gap-4">
<button class="px-6 py-3 rounded-full bg-primary text-white font-label-md flex items-center gap-2 transition-all hover:shadow-lg active:scale-95">
<span class="material-symbols-outlined" data-icon="coffee">coffee</span>
                    Hot Coffees
                </button>
<button class="px-6 py-3 rounded-full bg-white text-on-surface-variant font-label-md border border-outline-variant flex items-center gap-2 transition-all hover:bg-surface-container-low active:scale-95">
<span class="material-symbols-outlined" data-icon="ac_unit">ac_unit</span>
                    Cold Coffees
                </button>
<button class="px-6 py-3 rounded-full bg-white text-on-surface-variant font-label-md border border-outline-variant flex items-center gap-2 transition-all hover:bg-surface-container-low active:scale-95">
<span class="material-symbols-outlined" data-icon="emoji_food_beverage">emoji_food_beverage</span>
                    Teas
                </button>
<button class="px-6 py-3 rounded-full bg-white text-on-surface-variant font-label-md border border-outline-variant flex items-center gap-2 transition-all hover:bg-surface-container-low active:scale-95">
<span class="material-symbols-outlined" data-icon="icecream">icecream</span>
                    Frappuccino
                </button>
</div>
</section>
<!-- Grid of Drinks -->
<section class="max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop">
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-gutter">
<!-- Card 1 -->
<div class="glass-card rounded-xl overflow-hidden group hover:shadow-xl transition-all duration-300">
<div class="relative h-48 overflow-hidden">
<img class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" data-alt="A macro photograph of a steaming hot cafe latte in a minimalist white ceramic cup, featuring professional latte art on the surface. The lighting is soft and warm, highlighting the creamy texture of the milk foam against the rich coffee. The background is a clean, blurred coffee shop setting with earthy green and cream accents, reflecting a premium health-conscious aesthetic." src="https://lh3.googleusercontent.com/aida-public/AB6AXuCFJJc1CNkEL5H36EoUQvbSEAdJ0c6-qM9toqn_dwsrTIXJlEOITzDylyRFtPHp1L8q96ZeWVmnz9mGFSjCGPqtZnZFiS30D5pXfrs_ieWp9pKoF1pR-pjKycZ5B1LTCZlqtlyTOjUL8keuIXhnEYTQFzx_mD3OTg1wiEQZpVv1Ulmy3DMzIybosbj-gP0UQrI4aVHz_UQmmQY_nn_OrmJpT84rKXTMH7COlGZpbkmhVROBnRrNi5_UBTb7Lanh-_O1cGbjfCOzKrA"/>
<div class="absolute top-4 right-4 bg-primary-container text-white px-3 py-1 rounded-full font-label-md">190 kcal</div>
</div>
<div class="p-6">
<h3 class="font-headline-md text-headline-md text-primary mb-2">Caffè Latte</h3>
<p class="font-body-md text-on-surface-variant mb-4">Rich, full-bodied espresso with steamed milk and a light layer of foam.</p>
<div class="flex items-center justify-between">
<span class="text-success-green font-bold">12g Protein</span>
<button class="text-primary font-label-md hover:underline flex items-center gap-1">Customize <span class="material-symbols-outlined text-sm" data-icon="arrow_forward">arrow_forward</span></button>
</div>
</div>
</div>
<!-- Card 2 -->
<div class="glass-card rounded-xl overflow-hidden group hover:shadow-xl transition-all duration-300">
<div class="relative h-48 overflow-hidden">
<img class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" data-alt="A tall glass of iced caramel macchiato with visible layers of espresso and milk, topped with a delicate drizzle of golden caramel. The glass has condensation on the outside, conveying a refreshing and chilled mood. The scene is lit with bright, natural daylight in a modern, minimalist environment with soft mint green highlights and high-key whites." src="https://lh3.googleusercontent.com/aida-public/AB6AXuABgDu4r_Oi0YjvPDmYJXHFbym6zHujW_-1zgfEMQEifFCiBP1BYzvL0yeNiB7yxqhieCUU8kvJUZ8LG2ksNbBrQwUZBYaZ3SnRM5Wi6oW4ROqyFqJdYOsx94jhsNKDeIYvvAnbYUq_l9eGyWZ5_9SaKcajTwbvkBzIOsSFBkKHWapn0H72ajFVP0oNxcUoyudvVzG4jTQMqgwa6LfYE9M5NKw2jXEUMiMTNQsnhpXTzB041FpwqNVNx02-ZwPj4gWD3rdwjs5pCk0"/>
<div class="absolute top-4 right-4 bg-primary-container text-white px-3 py-1 rounded-full font-label-md">250 kcal</div>
</div>
<div class="p-6">
<h3 class="font-headline-md text-headline-md text-primary mb-2">Caramel Macchiato</h3>
<p class="font-body-md text-on-surface-variant mb-4">Freshly steamed milk with vanilla-flavored syrup marked with espresso.</p>
<div class="flex items-center justify-between">
<span class="text-success-green font-bold">7g Fat</span>
<button class="text-primary font-label-md hover:underline flex items-center gap-1">Customize <span class="material-symbols-outlined text-sm" data-icon="arrow_forward">arrow_forward</span></button>
</div>
</div>
</div>
<!-- Card 3 -->
<div class="glass-card rounded-xl overflow-hidden group hover:shadow-xl transition-all duration-300">
<div class="relative h-48 overflow-hidden">
<img class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" data-alt="An overhead view of a vibrant green Matcha Green Tea Latte in a transparent glass, showing a smooth and creamy texture. The green of the matcha is intense and natural, contrasted against a clean white stone surface. The lighting is diffused and serene, creating a calm and health-focused atmosphere typical of a premium modern wellness brand." src="https://lh3.googleusercontent.com/aida-public/AB6AXuAiwaiWnwBfwrJ06hPAsP5B88n9rowEQA7Cy7PCBO7wFxa7J6nNLqvQgsH-33m5_QlZnDLUALttkmCptecdd44CfRxGdBAZwnhGQ3bg5mVy9UjKlf0pjsDruL1qGpOz8FZgE9590Zk3mJDhDTjdMoXS68M5-I5yipB-TMowhA-2_XNZWiU7gr-036hNvOQEshXo3Lu3wCpJVGEtKuRTk2kC-pQRQFMdtdQTWHJMvSdIS7HnFFgf18EGCrUmdUHkG5kM30CLSV0gLHA"/>
<div class="absolute top-4 right-4 bg-primary-container text-white px-3 py-1 rounded-full font-label-md">240 kcal</div>
</div>
<div class="p-6">
<h3 class="font-headline-md text-headline-md text-primary mb-2">Matcha Latte</h3>
<p class="font-body-md text-on-surface-variant mb-4">Smooth and creamy matcha sweetened and served with steamed milk.</p>
<div class="flex items-center justify-between">
<span class="text-success-green font-bold">32g Carbs</span>
<button class="text-primary font-label-md hover:underline flex items-center gap-1">Customize <span class="material-symbols-outlined text-sm" data-icon="arrow_forward">arrow_forward</span></button>
</div>
</div>
</div>
<!-- Card 4 -->
<div class="glass-card rounded-xl overflow-hidden group hover:shadow-xl transition-all duration-300">
<div class="relative h-48 overflow-hidden">
<img class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" data-alt="A close-up shot of a cold brew coffee served in a tall glass over clear ice cubes. The coffee is dark and rich, with small bubbles at the top. The background is a minimalist, brightly lit cafe space with soft wooden textures and clean lines. The overall aesthetic is fresh, professional, and sophisticated, using a palette of deep coffee tones and bright neutrals." src="https://lh3.googleusercontent.com/aida-public/AB6AXuA0h7ttd5yWrv8bEQ0jldCNhrQyS5p1kPxsTAXtAEuPsCGFMITXKNoGs9ohYdUl3xh7f8Bft0VzKOxsBEiWNM0uCFDHU9LfncSoDdqiBiypUB3wDXdXOpiJmhJh85wtHzuHQkUnRdGAObtfjOXyhqY67YJf68CZnc1jnwiANjehSHlgRXFg33znSVqq9lS_f3LHcDxOVMFteDWHk37Nzb8gYRdZ1B_GBYFscMOUhbeKm_uDFnVXr_79R-R4FUsSM-o519gRN6XTbIM"/>
<div class="absolute top-4 right-4 bg-primary-container text-white px-3 py-1 rounded-full font-label-md">5 kcal</div>
</div>
<div class="p-6">
<h3 class="font-headline-md text-headline-md text-primary mb-2">Cold Brew</h3>
<p class="font-body-md text-on-surface-variant mb-4">Handcrafted in small batches daily, slow-steeped in cool water for 20 hours.</p>
<div class="flex items-center justify-between">
<span class="text-success-green font-bold">0g Sugar</span>
<button class="text-primary font-label-md hover:underline flex items-center gap-1">Customize <span class="material-symbols-outlined text-sm" data-icon="arrow_forward">arrow_forward</span></button>
</div>
</div>
</div>
</div>
</section>
<!-- CTA Section -->
<section class="mt-24 max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop">
<div class="bg-surface-container-high rounded-[2rem] p-12 flex flex-col md:flex-row items-center justify-between gap-12">
<div class="max-w-xl">
<h2 class="font-headline-lg text-headline-lg text-primary mb-4">Your Drink, Your Way</h2>
<p class="font-body-lg text-body-lg text-on-surface-variant">Don't settle for the default. Swap milk, adjust syrups, and see your macros update in real-time. Make every sip count toward your goals.</p>
</div>
<div class="flex flex-col sm:flex-row gap-4 w-full md:w-auto">
<button class="bg-primary text-white px-10 py-4 rounded-full font-label-md hover:bg-success-green transition-all shadow-md active:scale-95">Customize Your Drink</button>
<button class="bg-white border border-primary text-primary px-10 py-4 rounded-full font-label-md hover:bg-surface-container-low transition-all active:scale-95">View Menu</button>
</div>
</div>
</section>
</main>
<!-- BottomNavBar (Mobile Only) -->
<nav class="md:hidden fixed bottom-0 w-full z-50 flex justify-around items-center px-4 py-3 bg-surface-container dark:bg-surface-container-highest rounded-t-xl shadow-sm">
<div class="flex flex-col items-center justify-center bg-primary-container text-on-primary-container dark:bg-primary-fixed dark:text-on-primary-fixed rounded-full px-4 py-1">
<span class="material-symbols-outlined" data-icon="local_cafe">local_cafe</span>
<span class="font-label-md text-label-md">Explore</span>
</div>
<div class="flex flex-col items-center justify-center text-on-secondary-container dark:text-on-secondary-fixed-variant">
<span class="material-symbols-outlined" data-icon="calculate">calculate</span>
<span class="font-label-md text-label-md">Calculator</span>
</div>
<div class="flex flex-col items-center justify-center text-on-secondary-container dark:text-on-secondary-fixed-variant">
<span class="material-symbols-outlined" data-icon="favorite">favorite</span>
<span class="font-label-md text-label-md">Favorites</span>
</div>
<div class="flex flex-col items-center justify-center text-on-secondary-container dark:text-on-secondary-fixed-variant">
<span class="material-symbols-outlined" data-icon="history">history</span>
<span class="font-label-md text-label-md">Recent</span>
</div>
</nav>
<script>
        // Micro-interaction for drink cards
        document.querySelectorAll('.glass-card').forEach(card => {
            card.addEventListener('mouseenter', () => {
                card.style.transform = 'translateY(-8px)';
            });
            card.addEventListener('mouseleave', () => {
                card.style.transform = 'translateY(0)';
            });
        });

    // Search bar focus effect
        const searchInput = document.querySelector('input[type="text"]');
        const searchContainer = searchInput.parentElement;

    searchInput.addEventListener('focus', () => {
            searchContainer.classList.add('ring-2', 'ring-primary-container');
        });

    searchInput.addEventListener('blur', () => {
            searchContainer.classList.remove('ring-2', 'ring-primary-container');
        });`</script>`

</body></html>

<!-- Design System -->

<!DOCTYPE html>

<html class="light" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>NutriBucks - Drink Calculator</title>
<!-- Google Fonts -->
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;700&family=Source+Sans+3:wght@400;600&display=swap" rel="stylesheet"/>
<!-- Material Symbols -->
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            "colors": {
                    "outline": "#6f7a72",
                    "on-error-container": "#93000a",
                    "primary-container": "#006241",
                    "background": "#e6fff6",
                    "surface-container-low": "#dbfaf0",
                    "on-secondary-fixed-variant": "#384a46",
                    "on-secondary": "#ffffff",
                    "surface-container-high": "#d0efe4",
                    "tertiary-fixed": "#ffdad7",
                    "surface-container": "#d6f5ea",
                    "on-background": "#04201a",
                    "on-tertiary-fixed": "#3d0608",
                    "surface-container-highest": "#cbe9df",
                    "surface-bright": "#e6fff6",
                    "primary-fixed": "#a2f3c8",
                    "secondary": "#4f625d",
                    "on-secondary-fixed": "#0c1f1b",
                    "surface-dim": "#c2e1d6",
                    "outline-variant": "#bec9c0",
                    "error-container": "#ffdad6",
                    "surface": "#e6fff6",
                    "on-surface": "#04201a",
                    "on-secondary-container": "#556863",
                    "inverse-primary": "#87d7ad",
                    "on-tertiary-fixed-variant": "#76312f",
                    "tertiary-container": "#883f3c",
                    "on-primary-fixed": "#002113",
                    "secondary-fixed": "#d2e7e0",
                    "inverse-on-surface": "#d9f7ed",
                    "surface-tint": "#146b4a",
                    "on-tertiary": "#ffffff",
                    "primary": "#00482f",
                    "primary-fixed-dim": "#87d7ad",
                    "tertiary": "#6b2927",
                    "on-primary-container": "#8bdbb1",
                    "on-primary-fixed-variant": "#005235",
                    "tertiary-fixed-dim": "#ffb3ae",
                    "on-surface-variant": "#3f4943",
                    "on-tertiary-container": "#ffb9b4",
                    "white": "#FFFFFF",
                    "inverse-surface": "#1a352e",
                    "error": "#ba1a1a",
                    "surface-variant": "#cbe9df",
                    "secondary-container": "#d2e7e0",
                    "surface-container-lowest": "#ffffff",
                    "secondary-fixed-dim": "#b6cbc4",
                    "on-error": "#ffffff",
                    "accent-cream": "#F2F0EB",
                    "on-primary": "#ffffff",
                    "warm-gray": "#808080",
                    "success-green": "#00754A"
            },
            "borderRadius": {
                    "DEFAULT": "0.25rem",
                    "lg": "0.5rem",
                    "xl": "0.75rem",
                    "full": "9999px"
            },
            "spacing": {
                    "margin-desktop": "40px",
                    "gutter": "24px",
                    "unit": "8px",
                    "container-max": "1280px",
                    "margin-mobile": "16px"
            },
            "fontFamily": {
                    "headline-md": ["Plus Jakarta Sans"],
                    "caption": ["Source Sans Three"],
                    "label-md": ["Source Sans Three"],
                    "display-lg": ["Plus Jakarta Sans"],
                    "headline-lg": ["Plus Jakarta Sans"],
                    "headline-lg-mobile": ["Plus Jakarta Sans"],
                    "body-lg": ["Source Sans Three"],
                    "body-md": ["Source Sans Three"]
            },
            "fontSize": {
                    "headline-md": ["24px", {"lineHeight": "32px", "fontWeight": "600"}],
                    "caption": ["12px", {"lineHeight": "16px", "fontWeight": "400"}],
                    "label-md": ["14px", {"lineHeight": "20px", "letterSpacing": "0.01em", "fontWeight": "600"}],
                    "display-lg": ["48px", {"lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                    "headline-lg": ["32px", {"lineHeight": "40px", "fontWeight": "700"}],
                    "headline-lg-mobile": ["28px", {"lineHeight": "36px", "fontWeight": "700"}],
                    "body-lg": ["18px", {"lineHeight": "28px", "fontWeight": "400"}],
                    "body-md": ["16px", {"lineHeight": "24px", "fontWeight": "400"}]
            }
          },
        },
      }
    </script>
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        .scroll-hide::-webkit-scrollbar { display: none; }
        .glass-card {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.3);
        }
    </style>
</head>
<body class="bg-background text-on-background font-body-md selection:bg-primary-fixed selection:text-on-primary-fixed">
<!-- Top Navigation AppBar -->
<header class="fixed top-0 w-full z-50 flex justify-between items-center px-margin-mobile md:px-margin-desktop h-16 bg-surface dark:bg-inverse-surface">
<div class="flex items-center gap-4">
<span class="font-headline-md text-headline-md font-bold text-primary-container dark:text-primary-fixed">NutriBucks</span>
<nav class="hidden md:flex items-center gap-6 ml-8">
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-high dark:hover:bg-surface-container-highest transition-colors px-3 py-1 rounded-lg font-label-md text-label-md" href="#">Explore</a>
<a class="text-primary dark:text-primary-fixed font-bold hover:bg-surface-container-high transition-colors px-3 py-1 rounded-lg font-label-md text-label-md" href="#">Calculator</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-high transition-colors px-3 py-1 rounded-lg font-label-md text-label-md" href="#">Favorites</a>
</nav>
</div>
<div class="flex items-center gap-2">
<button class="material-symbols-outlined p-2 rounded-full hover:bg-surface-container-high transition-colors text-primary" data-icon="history">history</button>
<button class="material-symbols-outlined p-2 rounded-full hover:bg-surface-container-high transition-colors text-primary" data-icon="favorite">favorite</button>
<button class="md:hidden material-symbols-outlined p-2" data-icon="menu">menu</button>
</div>
</header>
<main class="pt-24 pb-32 px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto">
<div class="flex flex-col lg:flex-row gap-12 items-start">
<!-- Left Side: Visual Focus -->
<div class="w-full lg:w-1/2 sticky top-24">
<div class="relative group aspect-square lg:aspect-[4/5] rounded-[2rem] overflow-hidden bg-accent-cream shadow-sm flex items-center justify-center p-12">
<img alt="Starbucks Cup" class="object-contain w-full h-full drop-shadow-2xl transition-transform duration-700 group-hover:scale-105" data-alt="A professional studio photograph of a classic Starbucks white paper cup with the iconic green logo, placed centrally against a warm, soft cream-colored background. The lighting is bright and high-key, reflecting a fresh and healthy morning aesthetic. The composition is minimalist and clean, utilizing the primary brand colors of deep green and warm cream to create a premium health-conscious atmosphere. Subtle condensation droplets are visible on the cup, suggesting a fresh, chilled beverage inside." src="https://lh3.googleusercontent.com/aida-public/AB6AXuCzp2rgLCBDaxO6mThopGJfw1cjCI5TAiWdzDlamL8NhozZg_B1iUzxSxLKa3dQ7NHT_lcjNj2c0A7mGwoc9dR2LsWi5nCbtFPKaKB_sxC4j26RFMofLAf2Z0-hsDEehCNdxdY-OHNcZjhd8iKesTGvybMsEv956RShXvarKiXV_8Zt7vqdVupY7lBzI00gpCbs3JRBW4fAC5Jen2V68DnMyQO9Ua85aaGz0nA_QS_Xt8Tm9RdJcxHy79OC7JAJbF43dPc_pUYYlSA"/>
<!-- Floating Data Points (Micro-interaction layer) -->
<div class="absolute bottom-8 left-8 right-8 flex justify-between gap-4">
<div class="glass-card px-6 py-4 rounded-2xl shadow-sm animate-bounce" style="animation-duration: 3s;">
<p class="font-caption text-caption text-secondary uppercase tracking-wider">Caffeine</p>
<p class="font-headline-md text-headline-md text-primary" id="caffeine-display">150mg</p>
</div>
<div class="glass-card px-6 py-4 rounded-2xl shadow-sm animate-bounce" style="animation-duration: 4s;">
<p class="font-caption text-caption text-secondary uppercase tracking-wider">Estimated</p>
<p class="font-headline-md text-headline-md text-primary" id="calorie-display">120 kcal</p>
</div>
</div>
</div>
</div>
<!-- Right Side: Customization Controls -->
<div class="w-full lg:w-1/2 space-y-10">
<section>
<h1 class="font-headline-lg text-headline-lg text-on-surface mb-2">Caffè Latte</h1>
<p class="font-body-lg text-body-lg text-on-surface-variant">Customize your perfect cup while staying on track with your nutritional goals.</p>
</section>
<!-- Size Selection -->
<section class="space-y-4">
<div class="flex items-center justify-between">
<h3 class="font-label-md text-label-md text-primary uppercase tracking-widest">Select Size</h3>
<span class="text-caption text-secondary" id="size-label">Grande (16 fl oz)</span>
</div>
<div class="grid grid-cols-4 gap-3">
<button class="size-btn p-4 rounded-xl border border-outline-variant bg-surface-container-lowest hover:border-primary transition-all flex flex-col items-center gap-2 group" onclick="updateSize('Short', 8, 0.8)">
<span class="material-symbols-outlined text-secondary group-hover:text-primary" data-icon="coffee">coffee</span>
<span class="font-label-md">Short</span>
</button>
<button class="size-btn p-4 rounded-xl border border-outline-variant bg-surface-container-lowest hover:border-primary transition-all flex flex-col items-center gap-2 group" onclick="updateSize('Tall', 12, 1)">
<span class="material-symbols-outlined text-secondary group-hover:text-primary" data-icon="coffee" style="font-size: 28px;">coffee</span>
<span class="font-label-md">Tall</span>
</button>
<button class="size-btn p-4 rounded-xl border-2 border-primary bg-primary-fixed-dim text-on-primary-fixed transition-all flex flex-col items-center gap-2 group" onclick="updateSize('Grande', 16, 1.3)">
<span class="material-symbols-outlined text-primary" data-icon="coffee" style="font-size: 32px;">coffee</span>
<span class="font-label-md">Grande</span>
</button>
<button class="size-btn p-4 rounded-xl border border-outline-variant bg-surface-container-lowest hover:border-primary transition-all flex flex-col items-center gap-2 group" onclick="updateSize('Venti', 20, 1.6)">
<span class="material-symbols-outlined text-secondary group-hover:text-primary" data-icon="coffee" style="font-size: 36px;">coffee</span>
<span class="font-label-md">Venti</span>
</button>
</div>
</section>
<!-- Milk Options -->
<section class="space-y-4">
<h3 class="font-label-md text-label-md text-primary uppercase tracking-widest">Milk Options</h3>
<div class="flex flex-wrap gap-3">
<button class="milk-btn px-5 py-2.5 rounded-full border border-outline-variant bg-surface-container-lowest font-label-md hover:bg-primary-fixed-dim hover:border-primary transition-all active:scale-95" onclick="updateMilk('Whole', 1.5)">Whole</button>
<button class="milk-btn px-5 py-2.5 rounded-full border-2 border-primary bg-primary-fixed-dim text-on-primary-fixed font-label-md transition-all active:scale-95" onclick="updateMilk('2%', 1.2)">2% Milk</button>
<button class="milk-btn px-5 py-2.5 rounded-full border border-outline-variant bg-surface-container-lowest font-label-md hover:bg-primary-fixed-dim hover:border-primary transition-all active:scale-95" onclick="updateMilk('Non-fat', 0.8)">Non-fat</button>
<button class="milk-btn px-5 py-2.5 rounded-full border border-outline-variant bg-surface-container-lowest font-label-md hover:bg-primary-fixed-dim hover:border-primary transition-all active:scale-95" onclick="updateMilk('Soy', 1.1)">Soy</button>
<button class="milk-btn px-5 py-2.5 rounded-full border border-outline-variant bg-surface-container-lowest font-label-md hover:bg-primary-fixed-dim hover:border-primary transition-all active:scale-95" onclick="updateMilk('Oat', 1.4)">Oat</button>
<button class="milk-btn px-5 py-2.5 rounded-full border border-outline-variant bg-surface-container-lowest font-label-md hover:bg-primary-fixed-dim hover:border-primary transition-all active:scale-95" onclick="updateMilk('Almond', 0.9)">Almond</button>
</div>
</section>
<!-- Syrups & Sweeteners -->
<section class="space-y-4">
<h3 class="font-label-md text-label-md text-primary uppercase tracking-widest">Syrups</h3>
<div class="space-y-3">
<div class="flex items-center justify-between p-4 bg-surface-container rounded-xl border border-outline-variant/30">
<div class="flex items-center gap-3">
<span class="material-symbols-outlined text-secondary" data-icon="colors">colors</span>
<div>
<p class="font-label-md text-on-surface">Vanilla Syrup</p>
<p class="text-caption text-secondary">20 kcal per pump</p>
</div>
</div>
<div class="flex items-center gap-4">
<button class="w-8 h-8 rounded-full border border-primary text-primary flex items-center justify-center hover:bg-primary hover:text-white transition-colors" onclick="adjustSyrup(-1)">-</button>
<span class="font-headline-md w-6 text-center" id="syrup-count">2</span>
<button class="w-8 h-8 rounded-full border border-primary text-primary flex items-center justify-center hover:bg-primary hover:text-white transition-colors" onclick="adjustSyrup(1)">+</button>
</div>
</div>
</div>
</section>
<!-- Dynamic Nutritional Panel -->
<section class="bg-primary-container p-8 rounded-[2rem] text-on-primary-container shadow-xl">
<div class="flex items-center justify-between mb-8">
<h2 class="font-headline-md text-headline-md text-on-primary-container">Nutritional Profile</h2>
<span class="material-symbols-outlined text-primary-fixed" data-icon="nutrition">nutrition</span>
</div>
<div class="grid grid-cols-2 md:grid-cols-4 gap-6">
<div class="space-y-1">
<p class="text-caption opacity-80 uppercase font-semibold">Calories</p>
<p class="font-headline-md text-headline-md" id="calc-calories">190</p>
<div class="h-1 bg-on-primary-container/20 rounded-full">
<div class="h-full bg-primary-fixed rounded-full transition-all duration-500" id="bar-calories" style="width: 45%;"></div>
</div>
</div>
<div class="space-y-1">
<p class="text-caption opacity-80 uppercase font-semibold">Total Fat</p>
<p class="font-headline-md text-headline-md"><span id="calc-fat">7</span>g</p>
<div class="h-1 bg-on-primary-container/20 rounded-full">
<div class="h-full bg-primary-fixed rounded-full transition-all duration-500" id="bar-fat" style="width: 30%;"></div>
</div>
</div>
<div class="space-y-1">
<p class="text-caption opacity-80 uppercase font-semibold">Sugar</p>
<p class="font-headline-md text-headline-md"><span id="calc-sugar">18</span>g</p>
<div class="h-1 bg-on-primary-container/20 rounded-full">
<div class="h-full bg-primary-fixed rounded-full transition-all duration-500" id="bar-sugar" style="width: 60%;"></div>
</div>
</div>
<div class="space-y-1">
<p class="text-caption opacity-80 uppercase font-semibold">Caffeine</p>
<p class="font-headline-md text-headline-md"><span id="calc-caffeine">150</span>mg</p>
<div class="h-1 bg-on-primary-container/20 rounded-full">
<div class="h-full bg-primary-fixed rounded-full transition-all duration-500" id="bar-caffeine" style="width: 50%;"></div>
</div>
</div>
</div>
<button class="w-full mt-10 py-4 bg-primary-fixed text-on-primary-fixed rounded-xl font-headline-md flex items-center justify-center gap-3 hover:bg-white transition-all active:scale-95 shadow-lg">
<span class="material-symbols-outlined" data-icon="star">star</span>
                        Save Custom Drink
                    </button>
</section>
</div>
</div>
</main>
<!-- Bottom Navigation (Mobile Only) -->
<nav class="md:hidden fixed bottom-0 w-full z-50 flex justify-around items-center px-4 py-3 bg-surface-container dark:bg-surface-container-highest rounded-t-xl shadow-sm">
<div class="flex flex-col items-center justify-center text-on-secondary-container dark:text-on-secondary-fixed-variant group">
<span class="material-symbols-outlined" data-icon="local_cafe">local_cafe</span>
<span class="font-label-md text-label-md">Explore</span>
</div>
<div class="flex flex-col items-center justify-center bg-primary-container text-on-primary-container dark:bg-primary-fixed dark:text-on-primary-fixed rounded-full px-4 py-1 group">
<span class="material-symbols-outlined" data-icon="calculate">calculate</span>
<span class="font-label-md text-label-md">Calculator</span>
</div>
<div class="flex flex-col items-center justify-center text-on-secondary-container dark:text-on-secondary-fixed-variant group">
<span class="material-symbols-outlined" data-icon="favorite">favorite</span>
<span class="font-label-md text-label-md">Favorites</span>
</div>
<div class="flex flex-col items-center justify-center text-on-secondary-container dark:text-on-secondary-fixed-variant group">
<span class="material-symbols-outlined" data-icon="history">history</span>
<span class="font-label-md text-label-md">Recent</span>
</div>
</nav>
<script>
        // State
        let currentSizeMult = 1.3;
        let currentMilkMult = 1.2;
        let syrupCount = 2;

    const baseCals = 100;
        const baseFat = 4;
        const baseSugar = 12;
        const baseCaffeine = 115;

    function updateSize(name, oz, mult) {
            currentSizeMult = mult;
            document.getElementById('size-label').textContent =`${name} (${oz} fl oz)`;

    // Visual Update for buttons
            const buttons = document.querySelectorAll('.size-btn');
            buttons.forEach(btn => {
                btn.classList.remove('border-2', 'border-primary', 'bg-primary-fixed-dim', 'text-on-primary-fixed');
                btn.classList.add('border', 'border-outline-variant', 'bg-surface-container-lowest');
                if (btn.innerText.includes(name)) {
                    btn.classList.remove('border', 'border-outline-variant', 'bg-surface-container-lowest');
                    btn.classList.add('border-2', 'border-primary', 'bg-primary-fixed-dim', 'text-on-primary-fixed');
                }
            });

    calculate();
        }

    function updateMilk(name, mult) {
            currentMilkMult = mult;

    // Visual Update for buttons
            const buttons = document.querySelectorAll('.milk-btn');
            buttons.forEach(btn => {
                btn.classList.remove('border-2', 'border-primary', 'bg-primary-fixed-dim', 'text-on-primary-fixed');
                btn.classList.add('border', 'border-outline-variant', 'bg-surface-container-lowest');
                if (btn.innerText.includes(name)) {
                    btn.classList.remove('border', 'border-outline-variant', 'bg-surface-container-lowest');
                    btn.classList.add('border-2', 'border-primary', 'bg-primary-fixed-dim', 'text-on-primary-fixed');
                }
            });

    calculate();
        }

    function adjustSyrup(val) {
            syrupCount = Math.max(0, syrupCount + val);
            document.getElementById('syrup-count').textContent = syrupCount;
            calculate();
        }

    function calculate() {
            const finalCals = Math.round((baseCals * currentSizeMult * currentMilkMult) + (syrupCount * 20));
            const finalFat = Math.round((baseFat * currentSizeMult * currentMilkMult) * 10) / 10;
            const finalSugar = Math.round((baseSugar * currentSizeMult * currentMilkMult) + (syrupCount * 5));
            const finalCaffeine = Math.round(baseCaffeine * currentSizeMult);

    // Update Displays
            document.getElementById('calorie-display').textContent =`${finalCals} kcal`;
            document.getElementById('caffeine-display').textContent = `${finalCaffeine}mg`;

    document.getElementById('calc-calories').textContent = finalCals;
            document.getElementById('calc-fat').textContent = finalFat;
            document.getElementById('calc-sugar').textContent = finalSugar;
            document.getElementById('calc-caffeine').textContent = finalCaffeine;

    // Update Progress Bars (Relative scales)
            document.getElementById('bar-calories').style.width = Math.min(100, (finalCals / 400) * 100) + '%';
            document.getElementById('bar-fat').style.width = Math.min(100, (finalFat / 20) * 100) + '%';
            document.getElementById('bar-sugar').style.width = Math.min(100, (finalSugar / 50) * 100) + '%';
            document.getElementById('bar-caffeine').style.width = Math.min(100, (finalCaffeine / 300) * 100) + '%';
        }

    // Init
        calculate();`</script>`

</body></html>

<!-- NutriBucks - Calculator -->

<!DOCTYPE html>

<html lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>NutriBucks | Hot Coffees</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Source+Sans+3:wght@400;600&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<script id="tailwind-config">
        tailwind.config = {
          darkMode: "class",
          theme: {
            extend: {
              "colors": {
                      "outline": "#6f7a72",
                      "on-error-container": "#93000a",
                      "primary-container": "#006241",
                      "background": "#e6fff6",
                      "surface-container-low": "#dbfaf0",
                      "on-secondary-fixed-variant": "#384a46",
                      "on-secondary": "#ffffff",
                      "surface-container-high": "#d0efe4",
                      "tertiary-fixed": "#ffdad7",
                      "surface-container": "#d6f5ea",
                      "on-background": "#04201a",
                      "on-tertiary-fixed": "#3d0608",
                      "surface-container-highest": "#cbe9df",
                      "surface-bright": "#e6fff6",
                      "primary-fixed": "#a2f3c8",
                      "secondary": "#4f625d",
                      "on-secondary-fixed": "#0c1f1b",
                      "surface-dim": "#c2e1d6",
                      "outline-variant": "#bec9c0",
                      "error-container": "#ffdad6",
                      "surface": "#e6fff6",
                      "on-surface": "#04201a",
                      "on-secondary-container": "#556863",
                      "inverse-primary": "#87d7ad",
                      "on-tertiary-fixed-variant": "#76312f",
                      "tertiary-container": "#883f3c",
                      "on-primary-fixed": "#002113",
                      "secondary-fixed": "#d2e7e0",
                      "inverse-on-surface": "#d9f7ed",
                      "surface-tint": "#146b4a",
                      "on-tertiary": "#ffffff",
                      "primary": "#00482f",
                      "primary-fixed-dim": "#87d7ad",
                      "tertiary": "#6b2927",
                      "on-primary-container": "#8bdbb1",
                      "on-primary-fixed-variant": "#005235",
                      "tertiary-fixed-dim": "#ffb3ae",
                      "on-surface-variant": "#3f4943",
                      "on-tertiary-container": "#ffb9b4",
                      "white": "#FFFFFF",
                      "inverse-surface": "#1a352e",
                      "error": "#ba1a1a",
                      "surface-variant": "#cbe9df",
                      "secondary-container": "#d2e7e0",
                      "surface-container-lowest": "#ffffff",
                      "secondary-fixed-dim": "#b6cbc4",
                      "on-error": "#ffffff",
                      "accent-cream": "#F2F0EB",
                      "on-primary": "#ffffff",
                      "warm-gray": "#808080",
                      "success-green": "#00754A"
              },
              "borderRadius": {
                      "DEFAULT": "0.25rem",
                      "lg": "0.5rem",
                      "xl": "0.75rem",
                      "full": "9999px"
              },
              "spacing": {
                      "margin-desktop": "40px",
                      "gutter": "24px",
                      "unit": "8px",
                      "container-max": "1280px",
                      "margin-mobile": "16px"
              },
              "fontFamily": {
                      "headline-md": ["Plus Jakarta Sans"],
                      "caption": ["Source Sans 3"],
                      "label-md": ["Source Sans 3"],
                      "display-lg": ["Plus Jakarta Sans"],
                      "headline-lg": ["Plus Jakarta Sans"],
                      "headline-lg-mobile": ["Plus Jakarta Sans"],
                      "body-lg": ["Source Sans 3"],
                      "body-md": ["Source Sans 3"]
              },
              "fontSize": {
                      "headline-md": ["24px", {"lineHeight": "32px", "fontWeight": "600"}],
                      "caption": ["12px", {"lineHeight": "16px", "fontWeight": "400"}],
                      "label-md": ["14px", {"lineHeight": "20px", "letterSpacing": "0.01em", "fontWeight": "600"}],
                      "display-lg": ["48px", {"lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                      "headline-lg": ["32px", {"lineHeight": "40px", "fontWeight": "700"}],
                      "headline-lg-mobile": ["28px", {"lineHeight": "36px", "fontWeight": "700"}],
                      "body-lg": ["18px", {"lineHeight": "28px", "fontWeight": "400"}],
                      "body-md": ["16px", {"lineHeight": "24px", "fontWeight": "400"}]
              }
            },
          },
        }
    </script>
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        .custom-scrollbar::-webkit-scrollbar {
            width: 4px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
            background: transparent;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
            background: #bec9c0;
            border-radius: 10px;
        }
        .ambient-shadow {
            box-shadow: 0 10px 40px -10px rgba(0, 98, 65, 0.08);
        }
        body {
            background-color: #e6fff6;
        }
    </style>
</head>
<body class="font-body-md text-on-surface select-none overflow-x-hidden">
<!-- TopAppBar -->
<header class="fixed top-0 w-full z-50 flex justify-between items-center px-margin-mobile md:px-margin-desktop h-16 bg-surface dark:bg-inverse-surface">
<div class="flex items-center gap-4">
<span class="font-headline-md text-headline-md font-bold text-primary-container dark:text-primary-fixed">NutriBucks</span>
<nav class="hidden md:flex gap-6 ml-8">
<a class="text-primary dark:text-primary-fixed font-bold font-label-md text-label-md hover:bg-surface-container-high transition-colors px-3 py-1 rounded-lg" href="#">Explore</a>
<a class="text-on-surface-variant dark:text-surface-variant font-label-md text-label-md hover:bg-surface-container-high transition-colors px-3 py-1 rounded-lg" href="#">Calculator</a>
<a class="text-on-surface-variant dark:text-surface-variant font-label-md text-label-md hover:bg-surface-container-high transition-colors px-3 py-1 rounded-lg" href="#">Favorites</a>
</nav>
</div>
<div class="flex items-center gap-2">
<div class="hidden md:flex bg-surface-container-high px-4 py-2 rounded-full items-center gap-2">
<span class="material-symbols-outlined text-outline">search</span>
<input class="bg-transparent border-none focus:ring-0 text-sm w-48 text-on-surface" placeholder="Search menu..." type="text"/>
</div>
<button class="p-2 rounded-full hover:bg-surface-container-high dark:hover:bg-surface-container-highest transition-colors active:scale-95 duration-200">
<span class="material-symbols-outlined text-primary dark:text-primary-fixed-dim">history</span>
</button>
<button class="p-2 rounded-full hover:bg-surface-container-high dark:hover:bg-surface-container-highest transition-colors active:scale-95 duration-200">
<span class="material-symbols-outlined text-primary dark:text-primary-fixed-dim">favorite</span>
</button>
</div>
</header>
<main class="pt-24 pb-32 max-w-[1280px] mx-auto px-margin-mobile md:px-margin-desktop">
<!-- Header Section -->
<div class="mb-12">
<h1 class="font-headline-lg text-headline-lg text-primary mb-2">Hot Coffees</h1>
<p class="text-on-surface-variant font-body-lg text-body-lg max-w-2xl">Discover your perfect brew with detailed nutritional insights. From robust roasts to creamy classics, find the balance that fuels your day.</p>
</div>
<div class="flex flex-col md:flex-row gap-gutter">
<!-- Filter Sidebar -->
<aside class="w-full md:w-64 space-y-8 h-fit md:sticky md:top-24">
<div>
<h3 class="font-label-md text-label-md text-primary uppercase tracking-wider mb-4">Roast Type</h3>
<div class="space-y-3">
<label class="flex items-center gap-3 cursor-pointer group">
<input class="w-5 h-5 rounded border-outline text-primary-container focus:ring-primary" type="checkbox"/>
<span class="font-body-md text-body-md text-on-surface-variant group-hover:text-primary transition-colors">Blonde Roast</span>
</label>
<label class="flex items-center gap-3 cursor-pointer group">
<input checked="" class="w-5 h-5 rounded border-outline text-primary-container focus:ring-primary" type="checkbox"/>
<span class="font-body-md text-body-md text-on-surface-variant group-hover:text-primary transition-colors">Medium Roast</span>
</label>
<label class="flex items-center gap-3 cursor-pointer group">
<input class="w-5 h-5 rounded border-outline text-primary-container focus:ring-primary" type="checkbox"/>
<span class="font-body-md text-body-md text-on-surface-variant group-hover:text-primary transition-colors">Dark Roast</span>
</label>
</div>
</div>
<div>
<h3 class="font-label-md text-label-md text-primary uppercase tracking-wider mb-4">Caffeine Level</h3>
<div class="space-y-3">
<label class="flex items-center gap-3 cursor-pointer group">
<input class="w-5 h-5 border-outline text-primary-container focus:ring-primary" name="caffeine" type="radio"/>
<span class="font-body-md text-body-md text-on-surface-variant group-hover:text-primary transition-colors">Decaf</span>
</label>
<label class="flex items-center gap-3 cursor-pointer group">
<input checked="" class="w-5 h-5 border-outline text-primary-container focus:ring-primary" name="caffeine" type="radio"/>
<span class="font-body-md text-body-md text-on-surface-variant group-hover:text-primary transition-colors">Standard</span>
</label>
<label class="flex items-center gap-3 cursor-pointer group">
<input class="w-5 h-5 border-outline text-primary-container focus:ring-primary" name="caffeine" type="radio"/>
<span class="font-body-md text-body-md text-on-surface-variant group-hover:text-primary transition-colors">Extra Shot</span>
</label>
</div>
</div>
<div>
<h3 class="font-label-md text-label-md text-primary uppercase tracking-wider mb-4">Dietary Needs</h3>
<div class="flex flex-wrap gap-2">
<button class="px-4 py-1.5 rounded-full border border-outline-variant bg-white text-on-surface-variant font-label-md text-label-md hover:border-primary hover:text-primary transition-all">Vegan</button>
<button class="px-4 py-1.5 rounded-full border border-primary bg-primary-container text-on-primary-container font-label-md text-label-md">Dairy-Free</button>
<button class="px-4 py-1.5 rounded-full border border-outline-variant bg-white text-on-surface-variant font-label-md text-label-md hover:border-primary hover:text-primary transition-all">Low Sugar</button>
<button class="px-4 py-1.5 rounded-full border border-outline-variant bg-white text-on-surface-variant font-label-md text-label-md hover:border-primary hover:text-primary transition-all">Keto</button>
</div>
</div>
</aside>
<!-- Main Listing Area (Bento Grid Style) -->
<div class="flex-1">
<div class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-gutter">
<!-- Featured Product Card -->
<div class="lg:col-span-2 bg-white rounded-xl overflow-hidden ambient-shadow border border-accent-cream flex flex-col md:flex-row group transition-all duration-300 hover:-translate-y-1">
<div class="w-full md:w-1/2 h-64 md:h-full relative overflow-hidden">
<img class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" data-alt="A premium close-up of a steaming cafe latte with intricate latte art on a white ceramic surface. The lighting is soft and natural, emphasizing the creamy texture of the milk foam and the rich golden hue of the coffee. The background is a clean, minimalist cafe setting with soft greens and neutral cream tones, creating a fresh and inviting health-conscious aesthetic." src="https://lh3.googleusercontent.com/aida-public/AB6AXuAUX9eVSseyZMtStfzD6F3W1nVJ_83whgg6BiAZm6T8tRpI0UsSujvQDX-Ul7a1ZP2Ix60Vd39mLQsPANfDO1bNzeULuaeXSHpg2nncsO0EX9XGeYmKgoO4zLIBdT_Sljp84F5rRnkA11QJ5KTN8oPFZS5lkIdemRs0clToYLhj2km5q9dO00ccbp3D15pYRftWyhiCrYFwTdlC8G3QUmogBHOBf2OygH6D8nqtgR5QffP8-wFn6t25BwolwH-J-vwdXP9hF5JgMcw"/>
<div class="absolute top-4 left-4 bg-primary-container text-white px-3 py-1 rounded-full font-label-md text-label-md">Seasonal Favorite</div>
</div>
<div class="p-8 flex flex-col justify-between flex-1">
<div>
<div class="flex justify-between items-start mb-2">
<h2 class="font-headline-md text-headline-md text-primary">Signature Oatmilk Latte</h2>
<span class="material-symbols-outlined text-outline cursor-pointer hover:text-error transition-colors">favorite</span>
</div>
<p class="text-on-surface-variant mb-6 font-body-md text-body-md">Our signature espresso balanced with steamed creamy oatmilk and a touch of honey.</p>
<div class="space-y-4 mb-8">
<div class="flex justify-between items-end">
<span class="font-label-md text-label-md text-on-surface">Calories</span>
<span class="font-label-md text-label-md text-primary">120 kcal</span>
</div>
<div class="w-full bg-accent-cream h-1.5 rounded-full overflow-hidden">
<div class="bg-success-green h-full w-[35%] rounded-full"></div>
</div>
<div class="flex gap-4">
<div class="bg-surface-container px-3 py-2 rounded-lg flex-1">
<p class="text-caption font-caption text-outline">Sugar</p>
<p class="font-label-md text-label-md text-on-surface">8g</p>
</div>
<div class="bg-surface-container px-3 py-2 rounded-lg flex-1">
<p class="text-caption font-caption text-outline">Protein</p>
<p class="font-label-md text-label-md text-on-surface">3g</p>
</div>
<div class="bg-surface-container px-3 py-2 rounded-lg flex-1">
<p class="text-caption font-caption text-outline">Fat</p>
<p class="font-label-md text-label-md text-on-surface">5g</p>
</div>
</div>
</div>
</div>
<button class="w-full bg-primary-container text-white py-3 rounded-lg font-label-md text-label-md hover:bg-primary transition-colors flex items-center justify-center gap-2">
<span class="material-symbols-outlined text-sm">calculate</span>
                                Calculate Your Macros
                            </button>
</div>
</div>
<!-- Regular Card 1 -->
<div class="bg-white rounded-xl p-6 ambient-shadow border border-accent-cream transition-all duration-300 hover:-translate-y-1">
<div class="aspect-square rounded-lg mb-4 overflow-hidden">
<img class="w-full h-full object-cover" data-alt="A sleek glass of rich, dark americano coffee with a delicate layer of crema on top. The glass sits on a minimalist light wood table in a sun-drenched space. The overall atmosphere is professional and energetic, featuring high-key lighting and a palette dominated by deep coffee browns and crisp whites, perfectly aligned with a premium health-tech UI style." src="https://lh3.googleusercontent.com/aida-public/AB6AXuDyzqg5DnEnYvV30ZxyVHqusQQXTrmzQDDVGVTHdRCMOGXqpyTR12wzuxs_4BwTXZunsEJGeudwdgLO5723ZigAZ9cqf_eZilc4mL05jO-c5p8tsl6kHWhyVDOpe27BL5_JTBwTsX2omYUOU9h_bprbv27KqOyj0tEvS_T2RsE3pbj1JgeTS3b4_QEKc-GQ5RYVEmyZxP0XsU4zawj01oUdTwD-8xFrBfDYi3OJ5NvxHda8YkPsSf6dKc4Q0nmRzwh7MnE-2L5xmBM"/>
</div>
<h3 class="font-headline-md text-headline-md text-primary mb-1">Caffè Americano</h3>
<p class="text-on-surface-variant font-caption text-caption mb-4">Espresso shots topped with hot water.</p>
<div class="flex justify-between items-center pt-4 border-t border-accent-cream">
<div>
<p class="text-caption font-caption text-outline">Calories</p>
<p class="font-label-md text-label-md text-on-surface">15 kcal</p>
</div>
<span class="material-symbols-outlined text-primary-container bg-surface-container-low p-2 rounded-full">add</span>
</div>
</div>
<!-- Regular Card 2 -->
<div class="bg-white rounded-xl p-6 ambient-shadow border border-accent-cream transition-all duration-300 hover:-translate-y-1">
<div class="aspect-square rounded-lg mb-4 overflow-hidden">
<img class="w-full h-full object-cover" data-alt="A elegant white porcelain cup of cappuccino with a thick, velvety layer of foam dusted with a touch of cocoa powder. The shot is taken from a top-down perspective against a backdrop of fresh coffee beans. The lighting is bright and clean, emphasizing the organic textures and the calm, sophisticated mood of a high-end nutritional wellness platform." src="https://lh3.googleusercontent.com/aida-public/AB6AXuArrim1jRtl0qHYtKt0sA3GJhfTDXFIVxPGrrwYnO6wGG4_UFDN3L5GolDLrMefUau-QdGa01gFXG1Tcftee3U72sStn--Awtrn0aCL3S1doKPPX6YaRun6VOp5CgDRH9-iFv5eoTmX6QB3TKLbxwtEoNumazvY81APunwhYvrEnWFL_4cBNBLjPWGfk8kZWIrYMPCEVNn9lvBZkVRt9ZkqtHUr6RPuizrUXUfzZHOIY5ov2GYJGRNglanXOAc90CQfShSdmeSxabk"/>
</div>
<h3 class="font-headline-md text-headline-md text-primary mb-1">Cappuccino</h3>
<p class="text-on-surface-variant font-caption text-caption mb-4">Dark, rich espresso under a smoothed layer of foam.</p>
<div class="flex justify-between items-center pt-4 border-t border-accent-cream">
<div>
<p class="text-caption font-caption text-outline">Calories</p>
<p class="font-label-md text-label-md text-on-surface">140 kcal</p>
</div>
<span class="material-symbols-outlined text-primary-container bg-surface-container-low p-2 rounded-full">add</span>
</div>
</div>
<!-- Regular Card 3 -->
<div class="bg-white rounded-xl p-6 ambient-shadow border border-accent-cream transition-all duration-300 hover:-translate-y-1">
<div class="aspect-square rounded-lg mb-4 overflow-hidden">
<img class="w-full h-full object-cover" data-alt="A minimalist flat white served in a modern teal-colored ceramic cup. The coffee features a silky micro-foam with a simple heart-shaped art. The setting is bright and airy with soft shadows, using a color story of cool mint and warm cream. The mood is serene and focused, representing a premium lifestyle coffee experience for health-conscious individuals." src="https://lh3.googleusercontent.com/aida-public/AB6AXuDixz4t04YDlJ6-e_9-HPMbkC5Jrp7NLuk2XOaX-rv32MRIwXWcIhJnXL_6eRIjj7nzu-Jw4W4UX-mvyK-99KVaR0tr-ZpVjo_qwb_QwlPLrsXSrq84VuSsAf3EDSNZBejwzrTEx9cOmi84iYRo2EUaq1k2l3iLGYdtoG6NJ3IXwWfxadXvJ-uzs8YeIkRCvf3AhNEgfSL3j9XxwdJKIyobDF1Jyg2DcQV5XJAieUcjcEb3VWqVYQEYTh3UU1bG7OnhrV-vzp-dpag"/>
</div>
<h3 class="font-headline-md text-headline-md text-primary mb-1">Flat White</h3>
<p class="text-on-surface-variant font-caption text-caption mb-4">Ristretto shots with steamed whole milk.</p>
<div class="flex justify-between items-center pt-4 border-t border-accent-cream">
<div>
<p class="text-caption font-caption text-outline">Calories</p>
<p class="font-label-md text-label-md text-on-surface">170 kcal</p>
</div>
<span class="material-symbols-outlined text-primary-container bg-surface-container-low p-2 rounded-full">add</span>
</div>
</div>
<!-- Regular Card 4 -->
<div class="bg-white rounded-xl p-6 ambient-shadow border border-accent-cream transition-all duration-300 hover:-translate-y-1">
<div class="aspect-square rounded-lg mb-4 overflow-hidden">
<img class="w-full h-full object-cover" data-alt="A professional close-up of a caramel macchiato showing the beautiful layers of vanilla syrup, milk, espresso, and caramel drizzle in a tall glass. High-key studio lighting highlights the glossy finish of the caramel and the creamy layers. The visual style is crisp and modern, emphasizing the premium quality and ingredient transparency of the NutriBucks brand." src="https://lh3.googleusercontent.com/aida-public/AB6AXuBCyawlvFvvWqQdacbFAFNu7E_as8zDpJPL1Yd7jQps6dRTkMh4wWzK4I6PfLfUeWWzzGhoRRj841tKgcGCDwk0I19NzroFP-PqpGVG1pEt5Qf7HmzPgyAtgXgGhIjHNOdlfx6ZJWNLPtYC9Iit1pfNobC-sbzUP9LiSleofssLovLjpgDX_yV62JyScIx5F75GTKAphyw4uUmR6AvLzlLJ_43E0oGLIDSRvhpyqk2Yt3YuoeEy78xCz8769oWxeviuWi-nZ2nnsV8"/>
</div>
<h3 class="font-headline-md text-headline-md text-primary mb-1">Caramel Macchiato</h3>
<p class="text-on-surface-variant font-caption text-caption mb-4">Vanilla-flavored milk marked with espresso.</p>
<div class="flex justify-between items-center pt-4 border-t border-accent-cream">
<div>
<p class="text-caption font-caption text-outline">Calories</p>
<p class="font-label-md text-label-md text-on-surface">250 kcal</p>
</div>
<span class="material-symbols-outlined text-primary-container bg-surface-container-low p-2 rounded-full">add</span>
</div>
</div>
</div>
</div>
</div>
</main>
<!-- BottomNavBar (Mobile Only) -->
<nav class="md:hidden fixed bottom-0 w-full z-50 flex justify-around items-center px-4 py-3 bg-surface-container dark:bg-surface-container-highest rounded-t-xl shadow-sm">
<div class="flex flex-col items-center justify-center text-on-secondary-container dark:text-on-secondary-fixed-variant group transition-all">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">local_cafe</span>
<span class="font-label-md text-label-md mt-1">Explore</span>
</div>
<div class="flex flex-col items-center justify-center text-on-secondary-container dark:text-on-secondary-fixed-variant group transition-all">
<span class="material-symbols-outlined">calculate</span>
<span class="font-label-md text-label-md mt-1">Calculator</span>
</div>
<div class="flex flex-col items-center justify-center text-on-secondary-container dark:text-on-secondary-fixed-variant group transition-all">
<span class="material-symbols-outlined">favorite</span>
<span class="font-label-md text-label-md mt-1">Favorites</span>
</div>
<div class="flex flex-col items-center justify-center text-on-secondary-container dark:text-on-secondary-fixed-variant group transition-all">
<span class="material-symbols-outlined">history</span>
<span class="font-label-md text-label-md mt-1">Recent</span>
</div>
</nav>
<!-- Floating Action Button (FAB) -->
<button class="fixed bottom-24 right-6 md:bottom-8 md:right-8 bg-primary-container text-on-primary-container p-4 rounded-xl shadow-lg active:scale-90 transition-transform duration-150 z-40">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">add</span>
</button>
<script>
        // Simple Interaction logic
        document.querySelectorAll('.material-symbols-outlined').forEach(icon => {
            if (icon.textContent === 'favorite') {
                icon.addEventListener('click', function() {
                    const isFilled = this.style.fontVariationSettings.includes("'FILL' 1");
                    this.style.fontVariationSettings = isFilled ? "'FILL' 0" : "'FILL' 1";
                    this.style.color = isFilled ? '#6f7a72' : '#ba1a1a';
                });
            }
        });

    // Filter chips toggle
        document.querySelectorAll('aside button').forEach(button => {
            button.addEventListener('click', function() {
                const isActive = this.classList.contains('bg-primary-container');
                if (isActive) {
                    this.classList.remove('bg-primary-container', 'text-on-primary-container', 'border-primary');
                    this.classList.add('bg-white', 'text-on-surface-variant', 'border-outline-variant');
                } else {
                    this.classList.add('bg-primary-container', 'text-on-primary-container', 'border-primary');
                    this.classList.remove('bg-white', 'text-on-surface-variant', 'border-outline-variant');
                }
            });
        });`</script>`

</body></html>
