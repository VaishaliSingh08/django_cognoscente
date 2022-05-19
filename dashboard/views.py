from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, HttpResponse
from website.models import Contact, Services, Skills, Faqs, Reviews, Projects, Blog


# Create your views here.
def dashboard(request):
    if 'username' in request.session:
        return render(request, 'dashboard/index.html')
    return render(request, 'dashboard/404.html')

def queries(request):
    if 'username' in request.session:
        query = Contact.objects.order_by("-c_id_pk").values()
        query_count = Contact.objects.count()
        data = {"query": query, "query_count": query_count}
        return render(request, 'dashboard/product-list.html', data)
    return render(request, 'dashboard/404.html')


def view_query(request, id):
    if 'username' in request.session:
        p = Contact.objects.filter(c_id_pk=id).values()
        subject = p[0]['subject']
        name = p[0]['name']
        email = p[0]['email']
        message = p[0]['message']
        budget = p[0]['budget']
        code = p[0]['countrycode']
        contact = p[0]['contact_number']
        attachment = p[0]['attachment']
        attachments = Convert(attachment)
        len_attach = len(attachments)
        print(attachments)
        list_attach = []
        for i in attachments:
            i  = i.replace(",","")
            i  = i.replace("[","")
            i  = i.replace("]","")
            i  = i.replace("'","")
            i  = i.replace("'","")
            list_attach.append(i)

        date = p[0]['date']
        read = p[0]['read_status']
        read = 'true'
        con = Contact.objects.filter(c_id_pk=id).update(read_status=read)

        return render(request, 'dashboard/mailbox-view.html',
                      {'subject': subject, 'name': name, 'email': email, 'message': message, 'budget': budget,
                       'contact': contact, 'attachment': list_attach, 'len':len_attach,  'date': date, 'read': read, 'code': code})
    return render(request, 'dashboard/404.html')



def Convert(string):
    li = list(string.split(" "))
    return li

# Function to delete any product
def delete_query(request):
    if 'username' in request.session:
        Contact.objects.filter(c_id_pk=id).delete()
        return redirect('queries')
    return render(request, 'dashboard/404.html')


def dash_services(request):
    if 'username' in request.session:
        services = Services.objects.all()
        data = {"services": services}
        return render(request, 'dashboard/services_list.html', data)
    return render(request, 'dashboard/404.html')



def edit_services(request, id):
    if 'username' in request.session:
        p = Services.objects.filter(ser_id_pk=id).values()
        ser_id_pk = p[0]['ser_id_pk']
        ser_name = p[0]['ser_name']
        ser_header_img = p[0]['ser_header_img']
        ser_side_img = p[0]['ser_side_img']
        ser_desc_1 = p[0]['ser_desc_1']
        ser_desc_2 = p[0]['ser_desc_2']
        ser_one = p[0]['ser_one']
        ser_two = p[0]['ser_two']
        ser_three = p[0]['ser_three']
        ser_four = p[0]['ser_four']
        ser_five = p[0]['ser_five']
        ser_six = p[0]['ser_six']
        ser_seven = p[0]['ser_seven']
        ser_eight = p[0]['ser_eight']
        ser_nine = p[0]['ser_nine']
        ser_ten = p[0]['ser_ten']
        ser_eleven = p[0]['ser_eleven']
        ser_twelve = p[0]['ser_twelve']
        ser_heading = p[0]['head_text']
        ser_image = p[0]['ser_image']

        if request.method == "POST":
            ser_name = request.POST['ser_name']
            ser_desc_1 = request.POST['ser_desc_1']
            ser_desc_2 = request.POST['ser_desc_2']
            ser_heading = request.POST['ser_heading']
            ser_one = request.POST['ser_one']
            ser_two = request.POST['ser_two']
            ser_three = request.POST['ser_three']
            ser_four = request.POST['ser_four']
            ser_five = request.POST['ser_five']
            ser_six = request.POST['ser_six']
            ser_seven = request.POST['ser_seven']
            ser_eight = request.POST['ser_eight']
            ser_nine = request.POST['ser_nine']
            ser_ten = request.POST['ser_ten']
            ser_eleven = request.POST['ser_eleven']
            ser_twelve = request.POST['ser_twelve']

            fs = FileSystemStorage(location='media/services/')
            if request.FILES.get('ser_image'):
                myfile = request.FILES.get('ser_image')
                filename_1 = fs.save(myfile.name, myfile)
                f_name_1 = 'services/' + filename_1
                uploaded_file_url_1 = fs.url(f_name_1)
                uploaded_file_url_2 = ser_header_img
                uploaded_file_url_3 = ser_side_img
                ser = Services.objects.filter(ser_id_pk=id).update(ser_image=uploaded_file_url_1)
                return render(request, 'dashboard/services-edit.html',
                              {'ser_name': ser_name, 'ser_id_pk': ser_id_pk, 'ser_heading': ser_heading,
                               'ser_desc_1': ser_desc_1, 'ser_desc_2': ser_desc_2, 'ser_one': ser_one, 'ser_two': ser_two,
                               'ser_three': ser_three, 'ser_four': ser_four, 'ser_five': ser_five, 'ser_six': ser_six,
                               'ser_seven': ser_seven, 'ser_eight': ser_eight, 'ser_nine': ser_nine, 'ser_ten': ser_ten,
                               'ser_eleven': ser_eleven, 'ser_twelve': ser_twelve,
                               'ser_image': uploaded_file_url_1, 'ser_header_img': uploaded_file_url_2,
                               'ser_side_img': uploaded_file_url_3})

            if request.FILES.get('ser_header_img'):
                myfile1 = request.FILES.get('ser_header_img')
                filename_2 = fs.save(myfile1.name, myfile1)
                f_name_2 = 'services/' + filename_2
                uploaded_file_url_2 = fs.url(f_name_2)
                uploaded_file_url_1 = ser_image
                uploaded_file_url_3 = ser_side_img
                ser = Services.objects.filter(ser_id_pk=id).update(ser_header_img=uploaded_file_url_2)
                return render(request, 'dashboard/services-edit.html',
                              {'ser_name': ser_name, 'ser_id_pk': ser_id_pk, 'ser_heading': ser_heading,
                               'ser_desc_1': ser_desc_1, 'ser_desc_2': ser_desc_2, 'ser_one': ser_one, 'ser_two': ser_two,
                               'ser_three': ser_three, 'ser_four': ser_four, 'ser_five': ser_five, 'ser_six': ser_six,
                               'ser_seven': ser_seven, 'ser_eight': ser_eight, 'ser_nine': ser_nine, 'ser_ten': ser_ten,
                               'ser_eleven': ser_eleven, 'ser_twelve': ser_twelve,
                               'ser_image': uploaded_file_url_1, 'ser_header_img': uploaded_file_url_2,
                               'ser_side_img': uploaded_file_url_3})

            if request.FILES.get('ser_side_img'):
                myfile2 = request.FILES.get('ser_side_img')
                filename_3 = fs.save(myfile2.name, myfile2)
                f_name_3 = 'services/' + filename_3
                uploaded_file_url_3 = fs.url(f_name_3)
                uploaded_file_url_1 = ser_image
                uploaded_file_url_2 = ser_header_img
                ser = Services.objects.filter(ser_id_pk=id).update(ser_side_img=uploaded_file_url_3)
                return render(request, 'dashboard/services-edit.html',
                              {'ser_name': ser_name, 'ser_id_pk': ser_id_pk, 'ser_heading': ser_heading,
                               'ser_desc_1': ser_desc_1, 'ser_desc_2': ser_desc_2, 'ser_one': ser_one, 'ser_two':
                                   ser_two, 'ser_three': ser_three, 'ser_four': ser_four, 'ser_five': ser_five,
                               'ser_six': ser_six, 'ser_seven': ser_seven, 'ser_eight': ser_eight, 'ser_nine': ser_nine,
                               'ser_ten': ser_ten, 'ser_eleven': ser_eleven, 'ser_twelve': ser_twelve,
                               'ser_image': uploaded_file_url_1, 'ser_header_img': uploaded_file_url_2,
                               'ser_side_img': uploaded_file_url_3})

            ser = Services.objects.filter(ser_id_pk=id).update(ser_name=ser_name, ser_desc_1=ser_desc_1,
                                                               ser_desc_2=ser_desc_2, ser_one=ser_one, ser_two=ser_two,
                                                               ser_three=ser_three, ser_four=ser_four, ser_five=ser_five,
                                                               ser_six=ser_six, ser_seven=ser_seven, ser_eight=ser_eight,
                                                               ser_nine=ser_nine, ser_ten=ser_ten, ser_eleven=ser_eleven,
                                                               ser_twelve=ser_twelve, head_text=ser_heading)

            return render(request, 'dashboard/services-edit.html',
                          {'ser_name': ser_name, 'ser_id_pk': ser_id_pk, 'ser_heading': ser_heading,
                           'ser_desc_1': ser_desc_1, 'ser_desc_2': ser_desc_2, 'ser_one': ser_one, 'ser_two': ser_two,
                           'ser_three': ser_three, 'ser_four': ser_four, 'ser_five': ser_five, 'ser_six': ser_six,
                           'ser_seven': ser_seven, 'ser_eight': ser_eight, 'ser_nine': ser_nine, 'ser_ten': ser_ten,
                           'ser_eleven': ser_eleven, 'ser_twelve': ser_twelve, 'ser_header_img': ser_header_img,
                           'ser_side_img': ser_side_img, 'ser_image': ser_image})

        return render(request, 'dashboard/services-edit.html',
                      {'ser_name': ser_name, 'ser_image': ser_image, 'ser_id_pk': ser_id_pk,
                       'ser_header_img': ser_header_img, 'ser_side_img': ser_side_img, 'ser_desc_1': ser_desc_1,
                       'ser_desc_2': ser_desc_2, 'ser_one': ser_one, 'ser_two': ser_two, 'ser_three': ser_three,
                       'ser_four': ser_four, 'ser_five': ser_five, 'ser_six': ser_six, 'ser_seven': ser_seven,
                       'ser_eight': ser_eight, 'ser_nine': ser_nine, 'ser_ten': ser_ten, 'ser_eleven': ser_eleven,
                       'ser_twelve': ser_twelve, 'ser_heading': ser_heading})
    return render(request, 'dashboard/404.html')

def dash_skills(request):
    if 'username' in request.session:
        skills = Skills.objects.all()
        data = {"skills": skills}
        return render(request, 'dashboard/skills_list.html', data)
    return render(request, 'dashboard/404.html')

def edit_skills(request, id):
    if 'username' in request.session:
        p = Skills.objects.filter(s_id_pk=id).values()
        s_id_pk = p[0]['s_id_pk']
        skill_name = p[0]['skill_name']
        skill_image = p[0]['skill_image']

        if request.method == "POST":
            skill_name = request.POST['skill_name']
            fs = FileSystemStorage(location='media/skills/')
            if request.FILES.get('skill_image'):
                myfile = request.FILES.get('skill_image')
                filename_1 = fs.save(myfile.name, myfile)
                f_name_1 = 'skills/' + filename_1
                uploaded_file_url_1 = fs.url(f_name_1)
                ser = Skills.objects.filter(s_id_pk=id).update(skill_image=uploaded_file_url_1)
                return render(request, 'dashboard/skills-edit.html',
                              {'skill_name': skill_name, 'skill_image': skill_image, 's_id_pk': s_id_pk})

            skill = Skills.objects.filter(s_id_pk=id).update(skill_name=skill_name, skill_image=skill_image)

            return render(request, 'dashboard/skills-edit.html',
                          {'skill_name': skill_name, 'skill_image': skill_image, 's_id_pk': s_id_pk})

        return render(request, 'dashboard/skills-edit.html',
                      {'skill_name': skill_name, 'skill_image': skill_image, 's_id_pk': s_id_pk})

    return render(request, 'dashboard/404.html')


def delete_skill(request, id):
    if 'username' in request.session:
        Skills.objects.filter(s_id_pk=id).delete()
        return redirect('dash_skills')
    return render(request, 'dashboard/404.html')


def add_skill(request):
    if 'username' in request.session:
        if request.method == "POST":
            skill_name = request.POST['skill_name']
            myfile = request.FILES['skill_image']
            fs = FileSystemStorage(location='media/skills/')
            filename = fs.save(myfile.name, myfile)
            f_name = 'skills/' + filename
            uploaded_file_url = fs.url(f_name)
            print(uploaded_file_url)
            products = Skills.objects.create(skill_name=skill_name, skill_image=uploaded_file_url)

            products.save()

            return redirect('dash_skills')

        return render(request, 'dashboard/add_skills.html')
    return render(request, 'dashboard/404.html')


def dash_faqs(request):
    if 'username' in request.session:
        p = Faqs.objects.filter(f_id_pk=1).values()
        faq_heading = p[0]['faq_heading']
        faq_one = p[0]['faq_one']
        faq_two = p[0]['faq_two']
        faq_three = p[0]['faq_three']
        faq_four = p[0]['faq_four']
        faq_five = p[0]['faq_five']
        faq_six = p[0]['faq_six']
        faq_ans_1 = p[0]['faq_ans_1']
        faq_ans_2 = p[0]['faq_ans_2']
        faq_ans_3 = p[0]['faq_ans_3']
        faq_ans_4 = p[0]['faq_ans_4']
        faq_ans_5 = p[0]['faq_ans_5']
        faq_ans_6 = p[0]['faq_ans_6']
        p_1_name = p[0]['p_1_name']
        p_2_name = p[0]['p_2_name']
        p_3_name = p[0]['p_3_name']
        p_4_name = p[0]['p_4_name']
        p_5_name = p[0]['p_5_name']
        p_6_name = p[0]['p_6_name']
        p_1_value = p[0]['p_1_value']
        p_2_value = p[0]['p_2_value']
        p_3_value = p[0]['p_3_value']
        p_4_value = p[0]['p_4_value']
        p_5_value = p[0]['p_5_value']
        p_6_value = p[0]['p_6_value']

        if request.method == 'POST':
            faq_heading = request.POST['faq_heading']
            faq_one = request.POST['faq_one']
            faq_two = request.POST['faq_two']
            faq_three = request.POST['faq_three']
            faq_four = request.POST['faq_four']
            faq_five = request.POST['faq_five']
            faq_six = request.POST['faq_six']
            faq_ans_1 = request.POST['faq_ans_1']
            faq_ans_2 = request.POST['faq_ans_2']
            faq_ans_3 = request.POST['faq_ans_3']
            faq_ans_4 = request.POST['faq_ans_4']
            faq_ans_5 = request.POST['faq_ans_5']
            faq_ans_6 = request.POST['faq_ans_6']
            p_1_name = request.POST['p_1_name']
            p_2_name = request.POST['p_2_name']
            p_3_name = request.POST['p_3_name']
            p_4_name = request.POST['p_4_name']
            p_5_name = request.POST['p_5_name']
            p_6_name = request.POST['p_6_name']
            p_1_value = request.POST['p_1_value']
            p_2_value = request.POST['p_2_value']
            p_3_value = request.POST['p_3_value']
            p_4_value = request.POST['p_4_value']
            p_5_value = request.POST['p_5_value']
            p_6_value = request.POST['p_6_value']

            faqs = Faqs.objects.filter(f_id_pk=1).update(p_6_value=p_6_value, p_5_value=p_5_value, p_4_value=p_4_value,
                                                         p_3_value=p_3_value,
                                                         p_1_value=p_1_value, p_2_value=p_2_value, p_1_name=p_1_name,
                                                         p_2_name=p_2_name,
                                                         p_3_name=p_3_name, p_4_name=p_4_name, p_5_name=p_5_name,
                                                         p_6_name=p_6_name,
                                                         faq_one=faq_one, faq_two=faq_two, faq_three=faq_three,
                                                         faq_four=faq_four,
                                                         faq_five=faq_five, faq_six=faq_six, faq_ans_1=faq_ans_1,
                                                         faq_ans_2=faq_ans_2,
                                                         faq_ans_3=faq_ans_3, faq_ans_4=faq_ans_4, faq_ans_5=faq_ans_5,
                                                         faq_ans_6=faq_ans_6,
                                                         faq_heading=faq_heading)

            return render(request, 'dashboard/faqs.html',
                          {'p_6_value': p_6_value, 'p_5_value': p_5_value, 'p_4_value': p_4_value, 'p_3_value': p_3_value,
                           'p_1_value': p_1_value, 'p_2_value': p_2_value, 'p_1_name': p_1_name, 'p_2_name': p_2_name,
                           'p_3_name': p_3_name, 'p_4_name': p_4_name, 'p_5_name': p_5_name, 'p_6_name': p_6_name,
                           'faq_one': faq_one, 'faq_two': faq_two, 'faq_three': faq_three, 'faq_four': faq_four,
                           'faq_five': faq_five, 'faq_six': faq_six, 'faq_ans_1': faq_ans_1, 'faq_ans_2': faq_ans_2,
                           'faq_ans_3': faq_ans_3, 'faq_ans_4': faq_ans_4, 'faq_ans_5': faq_ans_5, 'faq_ans_6': faq_ans_6,
                           'faq_heading': faq_heading})

        return render(request, 'dashboard/faqs.html',
                      {'p_6_value': p_6_value, 'p_5_value': p_5_value, 'p_4_value': p_4_value, 'p_3_value': p_3_value,
                       'p_1_value': p_1_value, 'p_2_value': p_2_value, 'p_1_name': p_1_name, 'p_2_name': p_2_name,
                       'p_3_name': p_3_name, 'p_4_name': p_4_name, 'p_5_name': p_5_name, 'p_6_name': p_6_name,
                       'faq_one': faq_one, 'faq_two': faq_two, 'faq_three': faq_three, 'faq_four': faq_four,
                       'faq_five': faq_five, 'faq_six': faq_six, 'faq_ans_1': faq_ans_1, 'faq_ans_2': faq_ans_2,
                       'faq_ans_3': faq_ans_3, 'faq_ans_4': faq_ans_4, 'faq_ans_5': faq_ans_5, 'faq_ans_6': faq_ans_6,
                       'faq_heading': faq_heading})
    return render(request, 'dashboard/404.html')

def dash_reviews(request):
    if 'username' in request.session:
        reviews = Reviews.objects.all()
        data = {"reviews": reviews}
        return render(request, 'dashboard/reviews_list.html', data)
    return render(request, 'dashboard/404.html')


def add_review(request):
    if 'username' in request.session:
        if request.method == "POST":
            name = request.POST['name']
            rev = request.POST['review']
            desg = request.POST['desg']
            myfile = request.FILES['image']
            fs = FileSystemStorage(location='media/reviews/')
            filename = fs.save(myfile.name, myfile)
            f_name = 'reviews/' + filename
            uploaded_file_url = fs.url(f_name)
            print(uploaded_file_url)
            reviews = Reviews.objects.create(name=name, review=rev, desg=desg, image=uploaded_file_url)
            reviews.save()
            return redirect('dash_reviews')

        return render(request, 'dashboard/add_review.html')
    return render(request, 'dashboard/404.html')

def edit_reviews(request, id):
    if 'username' in request.session:
        p = Reviews.objects.filter(r_id_pk=id).values()
        r_id_pk = p[0]['r_id_pk']
        name = p[0]['name']
        rev = p[0]['review']
        desg = p[0]['desg']
        image = p[0]['image']

        if request.method == "POST":
            name = request.POST['name']
            rev = request.POST['review']
            desg = request.POST['desg']
            fs = FileSystemStorage(location='media/reviews/')
            if request.FILES.get('image'):
                myfile = request.FILES.get('image')
                filename_1 = fs.save(myfile.name, myfile)
                f_name_1 = 'image/' + filename_1
                uploaded_file_url_1 = fs.url(f_name_1)
                r = Reviews.objects.filter(r_id_pk=id).update(image=uploaded_file_url_1)
                return render(request, 'dashboard/edit_review.html',
                              {'r_id_pk': r_id_pk, 'name': name, 'desg': desg, 'rev': rev, 'image': image})

            rev = Reviews.objects.filter(r_id_pk=id).update(name=name, desg=desg, review=rev)
            return render(request, 'dashboard/edit_review.html',
                          {'r_id_pk': r_id_pk, 'name': name, 'desg': desg, 'rev': rev, 'image': image})

        return render(request, 'dashboard/edit_review.html',
                      {'r_id_pk': r_id_pk, 'name': name, 'desg': desg, 'rev': rev, 'image': image})
    return render(request, 'dashboard/404.html')

def delete_review(request, id):
    if 'username' in request.session:
        Reviews.objects.filter(r_id_pk=id).delete()
        return redirect('dash_reviews')
    return render(request, 'dashboard/404.html')


def dash_projects(request):
    if 'username' in request.session:
        projects = Projects.objects.all()
        data = {"projects": projects}
        return render(request, 'dashboard/projects_list.html', data)
    return render(request, 'dashboard/404.html')


def add_project(request):
    if 'username' in request.session:
        if request.method == "POST" or request.method == "FILES":
            p_name = request.POST['p_name']
            p_service = request.POST['p_service']
            p_desc_1 = request.POST['p_desc_1']
            p_desc_2 = request.POST['p_desc_2']
            p_skill_1 = request.POST['p_skill_1']
            p_skill_2 = request.POST['p_skill_2']
            p_skill_3 = request.POST['p_skill_3']
            p_skill_4 = request.POST['p_skill_4']
            p_skill_5 = request.POST['p_skill_5']
            p_skill_6 = request.POST['p_skill_6']
            p_skill_7 = request.POST['p_skill_7']
            p_skill_8 = request.POST['p_skill_8']
            p_skill_9 = request.POST['p_skill_9']
            p_skill_10 = request.POST['p_skill_10']
            myfile = request.FILES.get('p_img_1')
            myfile1 = request.FILES.get('p_img_2')
            myfile2 = request.FILES.get('p_img_3')
            myfile3 = request.FILES.get('p_img_4')
            uploaded_file_url = ''
            uploaded_file_url_1 = ''
            uploaded_file_url_2 = ''
            uploaded_file_url_3 = ''
            if request.FILES.get('p_img_1'):
                fs = FileSystemStorage(location='media/projects/')
                filename = fs.save(myfile.name, myfile)
                f_name = 'projects/' + filename
                uploaded_file_url = fs.url(f_name)

            if request.FILES.get('p_img_2'):
                fs = FileSystemStorage(location='media/projects/')
                filename = fs.save(myfile1.name, myfile1)
                f_name = 'projects/' + filename
                uploaded_file_url_1 = fs.url(f_name)
            if request.FILES.get('p_img_3'):
                fs = FileSystemStorage(location='media/projects/')
                filename = fs.save(myfile2.name, myfile2)
                f_name = 'projects/' + filename
                uploaded_file_url_2 = fs.url(f_name)
            if request.FILES.get('p_img_4'):
                fs = FileSystemStorage(location='media/projects/')
                filename = fs.save(myfile3.name, myfile3)
                f_name = 'projects/' + filename
                uploaded_file_url_3 = fs.url(f_name)

            projects = Projects.objects.create(p_name=p_name, p_skill_1=p_skill_1, p_skill_2=p_skill_2, p_skill_3=p_skill_3, p_skill_6=p_skill_6,p_skill_7=p_skill_7,p_skill_8=p_skill_8,p_skill_9=p_skill_9,p_skill_10=p_skill_10,p_skill_4=p_skill_4, p_skill_5=p_skill_5, p_service=p_service,
                                               p_desc_1=p_desc_1, p_desc_2=p_desc_2, p_img_1=uploaded_file_url,
                                               p_img_2=uploaded_file_url_1, p_img_3=uploaded_file_url_2,
                                               p_img_4=uploaded_file_url_3)
            projects.save()
            return redirect('dash_projects')

        return render(request, 'dashboard/add_project.html')
    return render(request, 'dashboard/404.html')

def delete_project(request, id):
    if 'username' in request.session:
        Projects.objects.filter(p_id_pk=id).delete()
        return redirect('dash_projects')
    return render(request, 'dashboard/404.html')


def edit_project(request, id):
    if 'username' in request.session:
        p = Projects.objects.filter(p_id_pk=id).values()
        p_id_pk = p[0]['p_id_pk']
        p_name = p[0]['p_name']
        p_service = p[0]['p_service']
        p_desc_1 = p[0]['p_desc_1']
        p_desc_2 = p[0]['p_desc_2']
        p_skill_1 = p[0]['p_skill_1']
        p_skill_2 = p[0]['p_skill_2']
        p_skill_3 = p[0]['p_skill_3']
        p_skill_4 = p[0]['p_skill_4']
        p_skill_5 = p[0]['p_skill_5']
        p_skill_6 = p[0]['p_skill_6']
        p_skill_7 = p[0]['p_skill_7']
        p_skill_8 = p[0]['p_skill_8']
        p_skill_9 = p[0]['p_skill_9']
        p_skill_10 = p[0]['p_skill_10']
        p_img_1 = p[0]['p_img_1']
        p_img_2 = p[0]['p_img_2']
        p_img_3 = p[0]['p_img_3']
        p_img_4 = p[0]['p_img_4']

        if request.method == "POST":
            p_name = request.POST['p_name']
            p_service = request.POST['p_service']
            p_desc_1 = request.POST['p_desc_1']
            p_desc_2 = request.POST['p_desc_2']
            p_skill_1 = request.POST['p_skill_1']
            p_skill_2 = request.POST['p_skill_2']
            p_skill_3 = request.POST['p_skill_3']
            p_skill_4 = request.POST['p_skill_4']
            p_skill_5 = request.POST['p_skill_5']
            p_skill_6 = request.POST['p_skill_6']
            p_skill_7 = request.POST['p_skill_7']
            p_skill_8 = request.POST['p_skill_8']
            p_skill_9 = request.POST['p_skill_9']
            p_skill_10 = request.POST['p_skill_10']
            myfile = request.FILES.get('p_img_1')
            myfile1 = request.FILES.get('p_img_2')
            myfile2 = request.FILES.get('p_img_3')
            myfile3 = request.FILES.get('p_img_4')

            project = Projects.objects.filter(p_id_pk=id).update(p_name=p_name, p_skill_1=p_skill_1, p_skill_2=p_skill_2,
                                                                 p_skill_3=p_skill_3, p_skill_4=p_skill_4,
                                                                 p_skill_5=p_skill_5,p_skill_6=p_skill_6,p_skill_7=p_skill_7,p_skill_8=p_skill_8,p_skill_9=p_skill_9,p_skill_10=p_skill_10, p_service=p_service,
                                                                 p_desc_1=p_desc_1, p_desc_2=p_desc_2)

            if request.FILES.get('p_img_1'):
                fs = FileSystemStorage(location='media/projects/')
                filename = fs.save(myfile.name, myfile)
                f_name = 'projects/' + filename
                uploaded_file_url = fs.url(f_name)
                project = Projects.objects.filter(p_id_pk=id).update(p_img_1=uploaded_file_url)
                uploaded_file_url_1 = p_img_2
                uploaded_file_url_2 = p_img_3
                uploaded_file_url_3 = p_img_4

                return render(request, 'dashboard/edit_project.html',
                              {'p_id_pk': p_id_pk, 'p_name': p_name, 'p_service': p_service, 'p_desc_1': p_desc_1,
                               'p_desc_2': p_desc_2, 'p_skill_5': p_skill_5, 'p_skill_4': p_skill_4, 'p_skill_3': p_skill_3,
                               'p_skill_2': p_skill_2, 'p_skill_6': p_skill_6,'p_skill_7': p_skill_7,'p_skill_8': p_skill_8,'p_skill_9': p_skill_9,'p_skill_10': p_skill_10, 'p_img_1': uploaded_file_url,
                               'p_img_2': uploaded_file_url_1, 'p_img_3': uploaded_file_url_2,
                               'p_img_4': uploaded_file_url_3})

            if request.FILES.get('p_img_2'):
                fs = FileSystemStorage(location='media/projects/')
                filename = fs.save(myfile1.name, myfile1)
                f_name = 'projects/' + filename
                uploaded_file_url_1 = fs.url(f_name)
                uploaded_file_url = p_img_1
                uploaded_file_url_2 = p_img_3
                uploaded_file_url_3 = p_img_4
                project = Projects.objects.filter(p_id_pk=id).update(p_img_2=uploaded_file_url_1)

                return render(request, 'dashboard/edit_project.html',
                              {'p_id_pk': p_id_pk, 'p_name': p_name, 'p_service': p_service, 'p_desc_1': p_desc_1,
                               'p_desc_2': p_desc_2, 'p_skill_5': p_skill_5, 'p_skill_4': p_skill_4, 'p_skill_3': p_skill_3,'p_skill_6': p_skill_6,'p_skill_7': p_skill_7,'p_skill_8': p_skill_8,'p_skill_9': p_skill_9,'p_skill_10': p_skill_10,
                               'p_skill_2': p_skill_2, 'p_skill_1': p_skill_1,
                               'p_img_1': uploaded_file_url, 'p_img_2': uploaded_file_url_1, 'p_img_3': uploaded_file_url_2,
                               'p_img_4': uploaded_file_url_3})

            if request.FILES.get('p_img_3'):
                fs = FileSystemStorage(location='media/projects/')
                filename = fs.save(myfile2.name, myfile2)
                f_name = 'projects/' + filename
                uploaded_file_url_2 = fs.url(f_name)
                uploaded_file_url_1 = p_img_2
                uploaded_file_url = p_img_1
                uploaded_file_url_3 = p_img_4
                project = Projects.objects.filter(p_id_pk=id).update(p_img_3=uploaded_file_url_2)
                return render(request, 'dashboard/edit_project.html',
                              {'p_id_pk': p_id_pk, 'p_name': p_name, 'p_service': p_service, 'p_desc_1': p_desc_1,
                               'p_desc_2': p_desc_2, 'p_skill_5': p_skill_5, 'p_skill_4': p_skill_4, 'p_skill_3': p_skill_3,'p_skill_6': p_skill_6,'p_skill_7': p_skill_7,'p_skill_8': p_skill_8,'p_skill_9': p_skill_9,'p_skill_10': p_skill_10,
                               'p_skill_2': p_skill_2, 'p_skill_1': p_skill_1, 'p_img_1': uploaded_file_url,
                               'p_img_2': uploaded_file_url_1, 'p_img_3': uploaded_file_url_2,
                               'p_img_4': uploaded_file_url_3})

            if request.FILES.get('p_img_4'):
                fs = FileSystemStorage(location='media/projects/')
                filename = fs.save(myfile3.name, myfile3)
                f_name = 'projects/' + filename
                uploaded_file_url_3 = fs.url(f_name)
                uploaded_file_url_1 = p_img_2
                uploaded_file_url_2 = p_img_3
                uploaded_file_url = p_img_1
                project = Projects.objects.filter(p_id_pk=id).update(p_img_4=uploaded_file_url_3)
                return render(request, 'dashboard/edit_project.html',
                              {'p_id_pk': p_id_pk, 'p_name': p_name, 'p_service': p_service, 'p_desc_1': p_desc_1,
                               'p_desc_2': p_desc_2, 'p_skill_5': p_skill_5, 'p_skill_4': p_skill_4, 'p_skill_3': p_skill_3,'p_skill_6': p_skill_6,'p_skill_7': p_skill_7,'p_skill_8': p_skill_8,'p_skill_9': p_skill_9,'p_skill_10': p_skill_10,
                               'p_skill_2': p_skill_2, 'p_skill_1': p_skill_1, 'p_img_1': uploaded_file_url,
                               'p_img_2': uploaded_file_url_1, 'p_img_3': uploaded_file_url_2,
                               'p_img_4': uploaded_file_url_3})

        return render(request, 'dashboard/edit_project.html',
                      {'p_id_pk': p_id_pk, 'p_name': p_name, 'p_service': p_service, 'p_desc_1': p_desc_1,
                       'p_desc_2': p_desc_2, 'p_skill_5': p_skill_5, 'p_skill_4': p_skill_4, 'p_skill_3': p_skill_3,
                       'p_skill_2': p_skill_2, 'p_skill_1': p_skill_1, 'p_img_1': p_img_1, 'p_img_2': p_img_2,
                       'p_img_3': p_img_3, 'p_img_4': p_img_4,'p_skill_6': p_skill_6,'p_skill_7': p_skill_7,'p_skill_8': p_skill_8,'p_skill_9': p_skill_9,'p_skill_10': p_skill_10})
    return render(request, 'dashboard/404.html')

def dash_blogs(request):
    if 'username' in request.session:
        blogs = Blog.objects.all()
        data = {'blogs': blogs}
        return render(request, 'dashboard/blog_list.html', data)
    return render(request, 'dashboard/404.html')

def edit_blog(request, id):
    if 'username' in request.session:
        p = Blog.objects.filter(b_id_pk=id).values()
        b_id_pk = p[0]['b_id_pk']
        b_name = p[0]['b_name']
        b_heading_1 = p[0]['b_heading_1']
        b_heading_2 = p[0]['b_heading_2']
        b_heading_3 = p[0]['b_heading_3']
        b_heading_4 = p[0]['b_heading_4']
        b_heading_5 = p[0]['b_heading_5']
        b_heading_6 = p[0]['b_heading_6']
        b_heading_7 = p[0]['b_heading_7']
        b_heading_8 = p[0]['b_heading_8']
        b_heading_9 = p[0]['b_heading_9']
        b_heading_10 = p[0]['b_heading_10']
        b_desc_1 = p[0]['b_desc_1']
        b_desc_2 = p[0]['b_desc_2']
        b_desc_3 = p[0]['b_desc_3']
        b_desc_4 = p[0]['b_desc_4']
        b_desc_5 = p[0]['b_desc_5']
        b_desc_6 = p[0]['b_desc_6']
        b_desc_7 = p[0]['b_desc_7']
        b_desc_8 = p[0]['b_desc_8']
        b_desc_9 = p[0]['b_desc_9']
        b_desc_10 = p[0]['b_desc_10']
        b_desc_11 = p[0]['b_desc_11']
        b_desc_12 = p[0]['b_desc_12']
        b_desc_13 = p[0]['b_desc_13']
        b_desc_14 = p[0]['b_desc_14']
        b_desc_15 = p[0]['b_desc_15']
        b_desc_16 = p[0]['b_desc_16']
        b_desc_17 = p[0]['b_desc_17']
        b_desc_18 = p[0]['b_desc_18']
        b_desc_19 = p[0]['b_desc_19']
        b_desc_20 = p[0]['b_desc_20']
        b_image_1 = p[0]['b_image_1']
        b_image_2 = p[0]['b_image_2']
        b_image_3 = p[0]['b_image_3']
        b_image_4 = p[0]['b_image_4']
        b_image_5 = p[0]['b_image_5']
        b_image_6 = p[0]['b_image_6']
        b_image_7 = p[0]['b_image_7']
        b_image_8 = p[0]['b_image_8']
        b_image_9 = p[0]['b_image_9']
        b_image_10 = p[0]['b_image_10']

        if request.method == "POST":
            b_heading = request.POST['b_heading']
            b_desc = request.POST['b_desc']
            myfile = request.FILES.get('b_image')
            blogs = Blog.objects.filter(b_id_pk=id).update(b_heading=b_heading, b_desc=b_desc)

            if request.FILES.get('b_image'):
                fs = FileSystemStorage(location='media/blogs/')
                filename = fs.save(myfile.name, myfile)
                f_name = 'blogs/' + filename
                uploaded_file_url = fs.url(f_name)
                blogs = Blog.objects.filter(b_id_pk=id).update(b_image=uploaded_file_url)

                return render(request, 'dashboard/edit_blog.html',
                              {'b_id_pk': b_id_pk, 'b_heading': b_heading,
                               'b_desc': b_desc, 'b_image': uploaded_file_url})

        return render(request, 'dashboard/edit_blog.html',
                      {'b_id_pk': b_id_pk, 'b_heading_1': b_heading_1, 'b_heading_3': b_heading_3,
                       'b_heading_4': b_heading_4, 'b_heading_5': b_heading_5, 'b_heading_6': b_heading_6,
                       'b_heading_7': b_heading_7, 'b_heading_8': b_heading_8, 'b_heading_9': b_heading_9,
                       'b_heading_10': b_heading_10, 'b_desc_1': b_desc_1, 'b_heading_2': b_heading_2, 'b_desc_2': b_desc_2,
                       'b_desc_3': b_desc_3, 'b_desc_4': b_desc_4, 'b_desc_5': b_desc_5, 'b_desc_6': b_desc_6,
                       'b_desc_7': b_desc_7, 'b_desc_8': b_desc_8, 'b_desc_9': b_desc_9, 'b_desc_10': b_desc_10,
                       'b_desc_11': b_desc_11, 'b_desc_12': b_desc_12, 'b_desc_13': b_desc_13, 'b_desc_14': b_desc_14,
                       'b_desc_15': b_desc_15, 'b_desc_16': b_desc_16, 'b_desc_17': b_desc_17, 'b_desc_18': b_desc_18,
                       'b_desc_19': b_desc_19, 'b_desc_20': b_desc_20, 'b_image_1': b_image_1, 'b_image_2': b_image_2,
                       'b_image_3': b_image_3, 'b_image_4': b_image_4, 'b_image_5': b_image_5, 'b_image_6': b_image_6,
                       'b_image_7': b_image_7, 'b_image_8': b_image_8, 'b_image_9': b_image_9, 'b_image_10': b_image_10,
                       'b_name': b_name})
    return render(request, 'dashboard/404.html')

def delete_blog(request, id):
    if 'username' in request.session:
        Blog.objects.filter(b_id_pk=id).delete()
        return redirect('dash_blogs')
    return render(request, 'dashboard/404.html')


def add_blog(request):
    if 'username' in request.session:
        if request.method == "POST":
            b_name = request.POST['b_name']
            b_heading_1 = request.POST['b_heading_1']
            b_heading_2 = request.POST['b_heading_2']
            b_heading_3 = request.POST['b_heading_3']
            b_heading_4 = request.POST['b_heading_4']
            b_heading_5 = request.POST['b_heading_5']
            b_heading_6 = request.POST['b_heading_6']
            b_heading_7 = request.POST['b_heading_7']
            b_heading_8 = request.POST['b_heading_8']
            b_heading_9 = request.POST['b_heading_9']
            b_heading_10 = request.POST['b_heading_10']
            b_desc_1 = request.POST['b_desc_1']
            b_desc_2 = request.POST['b_desc_2']
            b_desc_3 = request.POST['b_desc_3']
            b_desc_4 = request.POST['b_desc_4']
            b_desc_5 = request.POST['b_desc_5']
            b_desc_6 = request.POST['b_desc_6']
            b_desc_7 = request.POST['b_desc_7']
            b_desc_8 = request.POST['b_desc_8']
            b_desc_9 = request.POST['b_desc_9']
            b_desc_10 = request.POST['b_desc_10']
            b_desc_11 = request.POST['b_desc_11']
            b_desc_12 = request.POST['b_desc_12']
            b_desc_13 = request.POST['b_desc_13']
            b_desc_14 = request.POST['b_desc_14']
            b_desc_15 = request.POST['b_desc_15']
            b_desc_16 = request.POST['b_desc_16']
            b_desc_17 = request.POST['b_desc_17']
            b_desc_18 = request.POST['b_desc_18']
            b_desc_19 = request.POST['b_desc_19']
            b_desc_20 = request.POST['b_desc_20']
            b_image_1 = request.FILES['b_image_1']
            b_image_2 = request.FILES['b_image_2']
            b_image_3 = request.FILES['b_image_3']
            b_image_4 = request.FILES['b_image_4']
            b_image_5 = request.FILES['b_image_5']
            b_image_6 = request.FILES['b_image_6']
            b_image_7 = request.FILES['b_image_7']
            b_image_8 = request.FILES['b_image_8']
            b_image_9 = request.FILES['b_image_9']
            b_image_10 = request.FILES['b_image_10']

            fs = FileSystemStorage(location='media/blogs/')
            filename = fs.save(b_image_1.name, b_image_1)
            f_name = 'blogs/' + filename
            uploaded_file_url = fs.url(f_name)
            filename = fs.save(b_image_2.name, b_image_2)
            f_name = 'blogs/' + filename
            uploaded_file_url_2 = fs.url(f_name)
            filename = fs.save(b_image_3.name, b_image_3)
            f_name = 'blogs/' + filename
            uploaded_file_url_3 = fs.url(f_name)
            filename = fs.save(b_image_4.name, b_image_4)
            f_name = 'blogs/' + filename
            uploaded_file_url_4 = fs.url(f_name)
            filename = fs.save(b_image_5.name, b_image_5)
            f_name = 'blogs/' + filename
            uploaded_file_url_5 = fs.url(f_name)
            filename = fs.save(b_image_6.name, b_image_6)
            f_name = 'blogs/' + filename
            uploaded_file_url_6 = fs.url(f_name)
            filename = fs.save(b_image_7.name, b_image_7)
            f_name = 'blogs/' + filename
            uploaded_file_url_7 = fs.url(f_name)
            filename = fs.save(b_image_8.name, b_image_8)
            f_name = 'blogs/' + filename
            uploaded_file_url_8 = fs.url(f_name)
            filename = fs.save(b_image_9.name, b_image_9)
            f_name = 'blogs/' + filename
            uploaded_file_url_9 = fs.url(f_name)
            filename = fs.save(b_image_10.name, b_image_10)
            f_name = 'blogs/' + filename
            uploaded_file_url_10 = fs.url(f_name)

            blogs = Blog.objects.create(b_heading_1=b_heading_1, b_heading_2=b_heading_2, b_heading_3=b_heading_3,
                                        b_heading_4=b_heading_4, b_heading_5=b_heading_5, b_heading_6=b_heading_6,
                                        b_heading_7=b_heading_7, b_heading_8=b_heading_8, b_heading_9=b_heading_9,
                                        b_heading_10=b_heading_10, b_desc_1=b_desc_1, b_desc_2=b_desc_2, b_desc_3=b_desc_3,
                                        b_desc_4=b_desc_4, b_desc_5=b_desc_5, b_desc_6=b_desc_6, b_desc_7=b_desc_7,
                                        b_desc_8=b_desc_8, b_desc_9=b_desc_9, b_desc_10=b_desc_10, b_desc_11=b_desc_11,
                                        b_desc_12=b_desc_12, b_desc_13=b_desc_13, b_desc_14=b_desc_14, b_desc_15=b_desc_15,
                                        b_desc_16=b_desc_16, b_desc_17=b_desc_17, b_desc_18=b_desc_18, b_desc_19=b_desc_19,
                                        b_desc_20=b_desc_20, b_image_1=uploaded_file_url, b_image_2=uploaded_file_url_2,
                                        b_image_3=uploaded_file_url_3, b_image_4=uploaded_file_url_4,
                                        b_image_5=uploaded_file_url_5, b_image_6=uploaded_file_url_6,
                                        b_image_7=uploaded_file_url_7, b_image_8=uploaded_file_url_8,
                                        b_image_9=uploaded_file_url_9, b_image_10=uploaded_file_url_10, b_name=b_name)
            blogs.save()
            return redirect('dash_blogs')

        return render(request, 'dashboard/add_blog.html')
    return render(request, 'dashboard/404.html')

def logout(request):
    try:
        del request.session['username']
        return redirect('login')
    except KeyError:
        pass
        return redirect('login')

