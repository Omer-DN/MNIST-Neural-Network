# ייבוא הספריות הנחוצות
import tensorflow as tf  # ייבוא TensorFlow, ספריית קוד פתוח לפיתוח מודלים של למידת מכונה ובינה מלאכותית
from tensorflow import keras  # ייבוא keras מתוך TensorFlow, ממשק ברמה גבוהה לפיתוח מודלים
from tensorflow.keras import layers  # ייבוא מודול השכבות (layers) מתוך keras, המאפשר בניית שכבות של רשתות נוירונים

# טעינת הנתונים
(train_images, train_labels), (test_images, test_labels) = keras.datasets.mnist.load_data()
# הטעינת הנתונים מתוך מאגר ה-MNIST, הכולל תמונות של ספרות בכתב יד ותיוגים שלהן

# עיבוד הנתונים
train_images = train_images / 255.0  # נירמול תמונות האימון על ידי חלוקה ב-255 כדי לקבל ערכים בין 0 ל-1
test_images = test_images / 255.0  # נירמול תמונות הבדיקה באותה צורה

# בניית המודל
model = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # השכבה הראשונה: Flatten, הממירה את תמונת הקלט מ-28x28 ווקטור חד-ממדי
    layers.Dense(128, activation='relu'),  # השכבה השנייה: Dense, עם 128 נוירונים והפונקציה relu כפעילות (אקטיבציה)
    layers.Dense(10, activation='softmax')  # השכבה האחרונה: Dense, עם 10 נוירונים והפונקציה softmax לפלט סיווג של 10 קטגוריות
])

# קומפילציה של המודל
model.compile(optimizer='adam',  # אופטימייזר: adam, אלגוריתם אופטימיזציה שמתאים את קצב הלמידה במהלך האימון
              loss='sparse_categorical_crossentropy',  # פונקציית הפסד: sparse_categorical_crossentropy, מתאימה לסיווג מרובה קטגוריות
              metrics=['accuracy'])  # מדד ביצוע: דיוק (accuracy)

# אימון המודל
model.fit(train_images, train_labels, epochs=5)  # אימון המודל על נתוני האימון ל-5 תקופות (epochs)

# הערכת המודל
test_loss, test_acc = model.evaluate(test_images, test_labels)  # הערכת המודל על נתוני הבדיקה
print(f'\nTest accuracy: {test_acc}')  # הדפסת דיוק המודל על נתוני הבדיקה
