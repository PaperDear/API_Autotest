import allure

def allure_init(case):
    allure.dynamic.feature(case["feature"])  # behaviors
    allure.dynamic.story(case["story"])
    allure.dynamic.title(f'id={case["id"]},{case["title"]}')