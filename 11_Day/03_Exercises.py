
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(11))  # True
print(is_prime(25))  # False


# 2
def are_all_items_unique(lst):
    return len(lst) == len(set(lst))
print(are_all_items_unique([1, 2, 3, 4, 5]))  # True
print(are_all_items_unique([1, 2, 2, 4, 5]))  # Fa
# 3
def are_all_items_same_type(lst):
    return len(set(type(item) for item in lst)) == 1
print(are_all_items_same_type([1, 2, 3, 4]))  # True
print(are_all_items_same_type([1, "2", 3, 4]))  # False


# 4
def is_valid_variable(name):
    import re
    
    return bool(re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', name))
print(is_valid_variable("my_var"))  # True
print(is_valid_variable("2my_var"))  # False


# 5.
def most_spoken_languages():
   
    languages = {
        'English': 1500,
        'Mandarin Chinese': 1200,
        'Hindi': 600,
        'Spanish': 460,
        'French': 300,
        'Arabic': 274,
        'Bengali': 273,
        'Portuguese': 264,
        'Russian': 255,
        'Urdu': 230,
        'Indonesian': 199,
        'German': 135,
        'Japanese': 128,
        'Swahili': 98,
        'Marathi': 95,
        'Telugu': 93,
        'Turkish': 85,
        'Korean': 80,
        'Tamil': 78,
        'Punjabi': 77
    }
   
    return sorted(languages.items(), key=lambda x: x[1], reverse=True)[:10] 
print(most_spoken_languages())

def most_populated_countries():
   
    countries = {
        'China': 1444216107,
        'India': 1393409038,
        'United States': 332915073,
        'Indonesia': 276361783,
        'Pakistan': 225199937,
        'Brazil': 213993437,
        'Nigeria': 211400708,
        'Bangladesh': 166303498,
        'Russia': 145912025,
        'Mexico': 130262216,
        'Japan': 125584838,
        'Ethiopia': 120812698,
        'Philippines': 113866000,
        'Egypt': 104124440,
        'Vietnam': 98953541,
        'DR Congo': 95043920,
        'Turkey': 85561976,
        'Iran': 83992953,
        'Germany': 83783942,
        'Thailand': 69830779
    }
 
    return sorted(countries.items(), key=lambda x: x[1], reverse=True)[:10]  
print(most_populated_countries())