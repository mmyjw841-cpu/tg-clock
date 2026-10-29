import asyncio
import datetime
from pyrogram import Client

# بياناتك الشخصية المسجلة
api_id = 39133238
api_hash = "8b5b4cbfc58689e87a6eed8cf3e0e760"

# اسمك المزخرف المطلوب
MY_NAME = "𝑇𝐶 𝑀𝐼𝐷𝑂" 

app = Client("my_account", api_id=api_id, api_hash=api_hash)

# قاموس لتحويل أرقام الوقت العادية إلى أرقام مزخرفة
def get_fancy_time():
    now_str = datetime.datetime.now().strftime("%I:%M") # الوقت بدون AM/PM
    
    # خريطة تحويل الأرقام لأشكال مزخرفة فخمة
    normal_digits = "0123456789:"
    fancy_digits  = "𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿:"
    
    translation_table = str.maketrans(normal_digits, fancy_digits)
    return now_str.translate(translation_table)

async def main():
    async with app:
        print("تم تشغيل السكربت بنجاح!")
        last_time = ""
        while True:
            now = get_fancy_time()
            
            # لو الوقت اتغير، نحدّث الاسم فوراً
            if now != last_time:
                last_time = now
                # الشكل النهائي: اسمك + فاصل + الساعة المزخرفة (بدون منبه أو AM/PM)
                new_first_name = f"{MY_NAME} | {now}"
                
                try:
                    await app.update_profile(first_name=new_first_name)
                    print(f"تم تحديث الاسم إلى: {new_first_name}")
                except Exception as e:
                    print(f"حدث خطأ أثناء التحديث: {e}")
            
            # الانتظار لمدة 30 ثانية قبل الفحص التالي
            await asyncio.sleep(30)

app.run(main())
