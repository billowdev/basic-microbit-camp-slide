
Microbit

https://makecode.microbit.org/

  1. การ New Project  และตั้งชื่อโปรเจค

  2. บล็อก On start กับ forever

  3. คำสั่ง show ต่างๆ  Show leds, show icon, Show Strings, show number

  4. การ ดาวน์โหลด คำสั่ง

  5. การ อัปโหลด คำสั่ง 


  6. คำสั่ง input -> เมื่อกด ปุ่ม A ให้แสดง ตัวอักษร A 
					เมื่อกด ปุ่ม B ให้แสดง ตัวอักษร B
					  เมื่อกด ทั้งสองปุ่ม ให้แสดง รูป สี่เหลี่ยม

		โจทย์ 

		1 เมื่อเปิด "Microbit" ขึ้นมา เริ่มแรก   -> ให้แสดง รูปสี่เหลี่ยม ด้วยคำสั่ง Show leds 
		  และให้โชว์รูปจุด ตรงกลาง ตลอดเวลา

		2. เริ่มแรกให้แสดงรูป "เครื่องหมายถูกต้อง"  ด้วยคำสั่ง Show icons
		   และ แสดง icon หน้า ยิ้ม ตลอดเวลา

		3. เริ่มแรกให้แสดงรูป "กากบาท" ด้วยคำสั่ง show icons 
		   และ แสดง รูป หน้าบึ้ง ตลอดเวลา

		4. เริ่มแรกให้ แสดงตัวเลข 1 2 3
			และ ให้แสดง รูปอะไรก็ได้ ตลอดเวลา

	####################################
	temperature 
		show number(temperature)

	acceleration (mg)
		forever:
			on shake:
				show number(acceleration)

	light level
		show number(light level)

	############################

	7  ตัวแปร การ make variable  ,  Set ... to ...  , Change ... by ...

				1.1 สร้างตัวแปร ขึ้นมา 1 ตัว  ชื่อตัวแปร A
				  
				1.2 ตรง on Start ให้ใส่ค่าตัวเลขให้ตัวแปร A  ด้วยคำสั่ง Set ... to
					 -> Set A to 2 (ตัวเลขอะไรก็ได้)
				1.3 ให้ แสดงค่าจากตัวแปร A อยู่ตลอดเวลาใน forever

				2.1 ให้ เปลี่ยนค่า A ไป ทีละ 2 ด้วย คำสั่ง Change ... by ...


	  7.1 Math  ->   + - * /

			ตัวอย่าง 

			1. On shake:
			 	show number( Pic random(1-10) )

			2. on start:
				set A to pic random(1-10)
				set B to pic random(1-10)
				show string("A")
				show number(A)
				show string("B")
				show number(B)

	  8.1 คำสั่ง Loop

	  		8.1.1 repeat 

	  			โจทย์ ให้ใช้ตัวแปร A ในการ แสดง ตัวเลข 1 - 10 ด้วย repeat

	  			Set A to 1 
	  			repeat:
	  			change A by 1

			8.1.2 while   

				โจทย์ ให้ใช้ตัวแปร A ในการ เพิ่มค่าขึ้นทีละ 1 ไปเรื่อยๆ  ด้วย while loop 

					while true:
						show number(A)
						change A by 1

			8.1.3 for loop

				โจทย์ ให้ใช้ตัวแปร A ในการ โชว์ตัวเลข 0 - 10 ด้วย for loop

					for a from 0 to 10:
						show number(a)

	  8.2 logic  

	  	เงื่อนไข (conditions), การเปรียบเทียบ (comparison), 

	  	โจทย์
	  		one start:
	  			set A to 1
	  			repeat(4):
	  				show number (A)
	  				if a = 3 then:
	  					show icon ยิ้ม
	  				if a > 3 then:
	  					show icon อะไรก็ได้
	  	ตรรกศาสตร์ (Boolean) 

	  	โจทย์ 

	  		on start:
	  			set A to 1
	  			set B to 1

	  		forever:
	  			if A = 1 and B = 1 then:
	  				show number(A)
	  				show number(B)

	  			if A = 2 and B = 3 then:
	  				show string("A")
	  				show number(A)
	  				show string("B")
	  				show number(B)

	  			change A by 1
	  			change B by 1



 " ลองต่อ block ให้ โปรแกรมทำงาน " 

นับ 1 ถึง 10 แล้วนับ ถอยหลัง จนถึง 1

1 2.... 8 9 10 9 8... 2 1



9. thinkeracademy 

10 - OLED

11 - analog read pin ...

12 - servo

13 - setup crash sensor at pin ...

14 - moisture sensor
	- setup crash
		show number (moisture sensor)

