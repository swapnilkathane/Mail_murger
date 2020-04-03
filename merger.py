with open("names",'r',encoding='utf=8') as names_file:
    with open("body",'r',encoding='utf=8')as body_file:
        body=body_file.read()
        print(body)
        for name in names_file:
            mail="hello  "+name+body
            with open(name.strip(),'w',encoding='utf=8')as mail_file:
                mail_file.write(mail)