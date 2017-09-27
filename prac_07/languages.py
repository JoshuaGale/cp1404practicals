from prac_07.programming_language import ProgrammingLanguage


def run_tests():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(ruby)
    languages = [ruby, python, visual_basic]
    print("the dynamic language types are")
    [print(language.name) for language in languages if language.is_dynamic()]


if __name__ == "__main__":
    run_tests()
