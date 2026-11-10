def add_vat(price, vat_percent=18):
    """Qiymətə ƏDV əlavə edir."""
    return price + (price * vat_percent / 100)


def build_username(first, last, year=""):
    """İstifadəçi adı yaradır."""
    username = first.lower() + "." + last.lower()
    if year:
        username += str(year)
    return username


def add_bonus(scores, bonus):
    """Siyahıdakı balları artırır."""
    for i in range(len(scores)):
        scores[i] = min(100, scores[i] + bonus)


def with_bonus(scores, bonus):
    """Bonuslu yeni siyahı qaytarır."""
    new_scores = scores[:]
    for i in range(len(new_scores)):
        new_scores[i] = min(100, new_scores[i] + bonus)
    return new_scores


def average(*numbers):
    """Ədədlərin ortalamasını tapır."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def make_course(code, **details):
    """Kurs məlumatlarını dictionary qaytarır."""
    course = {"code": code}
    for key, value in details.items():
        course[key] = value
    return course


def make_student(name, score, group=""):
    """Tələbə dictionary-si yaradır."""
    student = {"name": name, "score": score}
    if group:
        student["group"] = group
    return student
