from sqlalchemy.orm import Session
from app.models.habits import Habit


def create_habit(db: Session, user_id: int, title: str, description: str = None):
    habit = Habit(title=title, description=description, user_id=user_id)
    
    db.add(habit)
    db.commit()
    db.refresh(habit)
    return habit

# Kullanıcının tüm alışkanlıklarını getir
def get_habits_by_user(db: Session, user_id: int, limit: int = 10, offset: int = 0):
    return db.query(Habit).filter(Habit.user_id == user_id).offset(offset).limit(limit).all()

# Alışkanlık ID'sine göre alışkanlığı getir
def get_habit_by_id(db: Session, habit_id: int):
    return db.query(Habit).filter(Habit.id == habit_id).first()

# Alışkanlığı sil
def delete_habit(db: Session, habit_id: int):
    habit = get_habit_by_id(db, habit_id)
    if habit:
        db.delete(habit)
        db.commit()
        
    return habit


#güncelleme fonksiyonu koymadık çünkü alışkanlıklar genellikle oluşturulduktan sonra çok fazla değişmezler. Eğer kullanıcı alışkanlığın adını veya açıklamasını değiştirmek isterse, bunu yeni bir alışkanlık oluşturarak yapabilir.