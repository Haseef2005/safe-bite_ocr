import easyocr
import cv2

class NutritionLabelOCR:
    def __init__(self, nutrition_keywords=None):
        # Default keywords if not provided
        # It would be better to provide as many nutrition-related keywords as possible
        self.nutrition_keywords = nutrition_keywords or [
            "calories", "protein", "carbohydrates", "sugar", "fat",
            "saturated fat", "trans fat", "fiber", "cholesterol", "sodium",
            "vitamin", "calcium", "iron", "potassium", "dietary fiber",
            "total fat", "monounsaturated fat", "polyunsaturated fat",
            "omega-3", "omega-6", "omega-9", "vitamin A", "vitamin B1",
            "vitamin B2", "vitamin B3", "vitamin B5", "vitamin B6",
            "vitamin B7", "vitamin B9", "vitamin B12", "vitamin C",
            "vitamin D", "vitamin E", "vitamin K", "magnesium", "phosphorus",
            "zinc", "selenium", "copper", "manganese", "fluoride", "iodine",
            "chromium", "molybdenum", "chloride", "biotin", "folate",
            "pantothenic acid", "riboflavin", "niacin", "thiamin",
            "pyridoxine", "cobalamin", "choline", "inositol", "carnitine",
            "glucose", "fructose", "lactose", "maltose", "sucrose",
            "starch", "glycogen", "dietary fiber", "soluble fiber",
            "insoluble fiber", "alcohol", "caffeine", "water", "ash",
            "energy", "polyols", "erythritol", "xylitol", "sorbitol",
            "mannitol", "isomalt", "lactitol", "maltitol", "hydrolyzed protein",
            "casein", "whey protein", "soy protein", "pea protein",
            "rice protein", "hemp protein", "collagen", "gelatin",
            "glutamine", "creatine", "beta-alanine", "citrulline",
            "taurine", "arginine", "leucine", "isoleucine", "valine",
            "methionine", "phenylalanine", "threonine", "tryptophan",
            "histidine", "lysine", "alanine", "asparagine", "aspartic acid",
            "cysteine", "glutamic acid", "glycine", "proline", "serine",
            "tyrosine", 'reduce fat milk', 'skim milk', 'whole milk', 'salt', 'carbohydrate'
        ]
        # Initialize EasyOCR Reader with English language
        self.reader = easyocr.Reader(['en']) 

    # This function suppose to make better OCR accuracy. but in this case, it's not necessary and it gets worse results.
    # def preprocess_image(self, image_path):
    #     image = cv2.imread(image_path)
    #     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #     _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    #     return thresh

    # This function is used to extract text from the image using EasyOCR.
    def extract_text(self, image_path):
        processed_image = image_path
        # EasyOCR expects image paths directly or numpy arrays
        results = self.reader.readtext(processed_image, detail=0)
        return "\n".join(results)

    # This function is used to filter out only the nutrition-related words from the OCR result.
    def get_nutrition_words(self, text):
        words_found = []
        for keyword in self.nutrition_keywords:
            if keyword in text.lower():
                words_found.append(keyword)
        return list(set(words_found))  

    # This function is used to process the image and return only the nutrition words found.
    def process_image(self, image_path):
        raw_text = self.extract_text(image_path)
        print(f"Raw Text Found:{raw_text}")
        return self.get_nutrition_words(raw_text)


# This is Example Usage
ocr = NutritionLabelOCR()
image_path = "./himage/n3.jpg"
nutrition_words = ocr.process_image(image_path)

print("Nutrition Words Found:")
print(nutrition_words)
