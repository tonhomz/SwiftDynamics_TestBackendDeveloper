[Swift Dynamics] Test Backend Developer (Python)

โจทย์ข้อที่ 5 ได้ทำ API ดังนี้
1. School API
- create school
- school list (can filter by name)
- update school
- delete school
2. Classroom API
- create classroom
- classroom list
- update classroom
- delete classroom
3. Teacher API
- create teacher
- teacher list (can filter by firstname, lastname, gender)
- update teacher
- delete teacher
4. Student API
- create student
- student list (can filter by firstname, lastname, gender)
- update student
- delete student

โดย API สำหรับการแสดง detail จากความรู้ในเรื่อง database หนูคิดว่าอาจต้องมีการกำหนด Foreign Key เพื่อให้เป็นค่าที่สามารถอ้างถึงได้ข้าม table ตามความสัมพันธ์ที่กำหนดค่ะ เช่น 
- student จะต้องมีการกำหนดว่าอยู่ classroom ไหน เป็นความสัมพันธ์แบบ 1 M เนื่องจาก 1 classroom สามารถมีนักเรียนได้หลายคน จึงอาจสร้าง table อีก 1 table แยกออกมาเก็บค่า id ของ student และ classroom โดยเฉพาะเพื่อลดความซ้ำซ้อนของข้อมูลในฐานข้อมูล เมื่อต้องการสร้าง api สำหรับ student list (filter by classroom) ก็จะสามารถ query ข้อมูลเฉพาะ student ใน classroom นั้นๆ ได้ ถ้าต้องการข้อมูล firstname, lastname, gender, grade, section ก็จะสามารถดึงข้อมูลได้ผ่าน id ที่เป็น foreign key ค่ะ รวมถึงถ้าต้องการสร้าง api สำหรับ classroom detail (show list of student) ก็จะสามารถดึงข้อมูลจาก table นี้และแสดงผลลัพธ์เป็นกลุ่มของ student ในแต่ละ classroom ได้ค่ะ
  
