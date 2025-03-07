BASE = [
    "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap",
    "/theme.css",
    "https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
]

base_style = {
    "font_family": "Inter",
    "@keyframes slideRight": {
        "from": {
            "transform": "translateX(100%)",
            "opacity": "0"
        },
        "to": {
            "transform": "translateX(0)",
            "opacity": "1" 
        }
    },
    "@keyframes slideLeft": {
        "from": {
            "transform": "translateX(0)",
            "opacity": "1"
        },
        "to": {
            "transform": "translateX(-100%)",
            "opacity": "0" 
        }
    }
}
