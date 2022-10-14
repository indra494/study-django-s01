from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Member

# Create your tests here.
def create_member(mem_id, mem_name, mem_age) :
    return Member.objects.create(mem_id=mem_id, mem_name=mem_name, mem_age=mem_age, mem_join_date=timezone.now())


class MemberViewTests(TestCase):

    def test_member_list_case01(self):
        member01 = create_member('indra71','인드라71',20)
        response = self.client.get(reverse('join:indexView'))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['member_list'], [member01])

    def test_member_list_case02(self):
        member01 = create_member('indra71','인드라71',20)
        member02 = create_member('indra72','인드라72',20)        

        response = self.client.get(reverse('join:indexView'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['member_list'], [member02] + [member01])

    def test_member_list_case03(self):
        member01 = create_member('indra71','인드라71',20)

        response = self.client.get(reverse('join:indexView'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, member01.mem_name)    

    def test_member_insert_case01(self) :
        member01 = Member('indra71','인드라71',20)

        response = self.client.post(
              reverse('join:save')
            , {'mem_id' : member01.mem_id, 'mem_name' : member01.mem_name, 'mem_age' : member01.mem_age}
        );
        self.assertEqual(response.status_code, 302)
             
        response = self.client.get(reverse('join:indexView'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, member01.mem_name)

    def test_member_detail_case01(self) :
        member01 = create_member('indra71','인드라71',20)

        url = reverse('join:detailView', args=(member01.mem_id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, member01.mem_name)

class MemberModelTests(TestCase):

    def test_is_member_adult_case01(self):
        member = Member('indra71','인드라71',20)
        self.assertIs(member.isAdult(),True)   

    def test_is_member_adult_case02(self):
        member = Member('indra71','인드라71',19)
        self.assertIs(member.isAdult(),False)   

    def test_is_member_adult_case03(self):
        member = Member('indra71','인드라71',22)
        self.assertIs(member.isAdult(),True)                   