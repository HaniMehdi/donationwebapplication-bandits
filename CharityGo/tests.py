from django.test import TestCase
from django.contrib.auth.models import User

from CharityGo.models import NGO, Donation, Donor, Campaign, SponsorRequest

# Create your tests here.

class NGOTest(TestCase):

    def setUp(self):
        # Pre-requisites for the test        
        return super().setUp()


    def test_ngos_for_correct_insertions(self):
        user = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user, ngo_name='Test NGO1', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user)
        #Checking if inserted data is same as provided
        self.assertEqual(ngo.ngo_name, 'Test NGO1')
        self.assertEqual(ngo.ngo_address, 'Test Address')
        self.assertEqual(ngo.ngo_description, 'Test Description')
        self.assertEqual(ngo.ngo_phone, '1234567890')
        self.assertEqual(ngo.ngo_bank_name, 'Test Bank')
        self.assertEqual(ngo.ngo_account_title, 'Test Account')
        self.assertEqual(ngo.ngo_account_no, '123456789')
        self.assertEqual(ngo.ngo_image, 'test_image.jpg')
        self.assertEqual(ngo.user.username, 'test1')
        self.assertEqual(ngo.created_by.username, 'test1')


    def test_ngo_for_auto_datecreated_on_record_insertion(self):
        user = User.objects.create_superuser(username='test2', email='test2@gmail.com', password='abc123def2')
        ngo = NGO.objects.create(user=user, ngo_name='Test NGO2', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user)
        #Checking if date_created is automatically set on record insertion
        self.assertIsNotNone(ngo.date_created)

    
    def test_ngo_table_for_auto_createdby_on_insertion(self):
        user1 = User.objects.create_superuser(username='test3', email='test3@gmail.com', password='abc123def3')        
        ngo1 = NGO.objects.create(user=user1, ngo_name='Test NGO3', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg')
        #Checking if created_by is automatically set on record insertion
        self.assertIsNotNone(ngo1.created_by)


    def test_ngo_for_auto_uuid_on_record_insertion(self):
        user = User.objects.create_superuser(username='test4', email='test4@gmail.com', password='abc123def2')
        ngo = NGO.objects.create(user=user, ngo_name='Test NGO4', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user)
        #Checking if uuid is automatically set on record insertion
        self.assertIsNotNone(ngo.uuid)


    def test_ngo_table_for_duplicate_ngos(self):
        user1 = User.objects.create_superuser(username='test5', email='test5@gmail.com', password='abc123def3')
        user2 = User.objects.create_superuser(username='test6', email='test6@gmail.com', password='abc123def4')
        ngo1 = NGO.objects.create(user=user1, ngo_name='Test NGO5', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1)    
        #Checking if NGO table allows insertion with same NGO name, error must be thrown 
        with self.assertRaises(ValueError):
            ngo2 = NGO.objects.create(user=user2, ngo_name='Test NGO5', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user2)
            
    
    def test_ngo_table_for_required_fields_on_record_creation(self):
        user1 = User.objects.create_superuser(username='test7', email='test1@gmail.com', password='abc123def1')
        user2 = User.objects.create_superuser(username='test8', email='test2@gmail.com', password='abc123def1')
        user3 = User.objects.create_superuser(username='test9', email='test3@gmail.com', password='abc123def1')
        user4 = User.objects.create_superuser(username='test10', email='test4@gmail.com', password='abc123def1')
        user5 = User.objects.create_superuser(username='test11', email='test5@gmail.com', password='abc123def1')
        user6 = User.objects.create_superuser(username='test12', email='test6@gmail.com', password='abc123def1')
        user7 = User.objects.create_superuser(username='test13', email='test7@gmail.com', password='abc123def1')
        user8 = User.objects.create_superuser(username='test14', email='test8@gmail.com', password='abc123def1')
        #Checking if NGO table allows insertion with required values = None, error must be thrown
        with self.assertRaises(ValueError):
            NGO.objects.create(user=user1, ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1)
            NGO.objects.create(user=user2, ngo_name='Test NGO6', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user2)
            NGO.objects.create(user=user3, ngo_name='Test NGO7', ngo_address='Test Address', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user3)
            NGO.objects.create(user=user4, ngo_name='Test NGO8', ngo_address='Test Address', ngo_description='Test Description',
                                 ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user4)
            NGO.objects.create(user=user5, ngo_name='Test NGO9', ngo_address='Test Address', ngo_description='Test Description',
                                 ngo_phone='1234567890', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user5)
            NGO.objects.create(user=user6, ngo_name='Test NGO10', ngo_address='Test Address', ngo_description='Test Description',
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user6)
            NGO.objects.create(user=user7, ngo_name='Test NGO11', ngo_address='Test Address', ngo_description='Test Description',
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', 
                                 ngo_image='test_image.jpg', created_by=user7)
            NGO.objects.create(user=user8, ngo_name='Test NGO12', ngo_address='Test Address', ngo_description='Test Description',
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 created_by=user8)
            
            
    
    def test_ngo_for_auto_datedupdated_on_record_updation(self):
        user = User.objects.create_superuser(username='test15', email='test2@gmail.com', password='abc123def2')
        ngo = NGO.objects.create(user=user, ngo_name='Test NGO13', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user)
        ngo.ngo_name = 'Test1'
        ngo.update()
        #Checking if date_updated is automatically set on record updation
        self.assertIsNotNone(ngo.date_updated)

    
    def test_ngo_for_auto_updatedby_on_record_updation(self):
        user = User.objects.create_superuser(username='test16', email='test2@gmail.com', password='abc123def2')
        ngo = NGO.objects.create(user=user, ngo_name='Test NGO14', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user)
        ngo.ngo_name = 'Test1'
        ngo.update()
        #Checking if updated_by is automatically set on record updation
        self.assertIsNotNone(ngo.updated_by)

    
    def test_ngo_for_auto_voidedby_on_record_deletion(self):
        user = User.objects.create_superuser(username='test17', email='test2@gmail.com', password='abc123def2')
        ngo1 = NGO.objects.create(user=user, ngo_name='Test NGO15', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user)
        ngo1.delete()
        #Checking if voidedby is automatically set on record deletion
        self.assertIsNotNone(ngo1.voided_by)

    
    def test_ngo_for_auto_voidreason_on_record_deletion(self):
        user = User.objects.create_superuser(username='test18', email='test3@gmail.com', password='abc123def2')
        ngo = NGO.objects.create(user=user, ngo_name='Test NGO16', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user)
        ngo.delete()
        #Checking if void_reason is automatically set on record deletion
        self.assertIsNotNone(ngo.void_reason)

    
    def test_ngo_for_auto_datevoided_on_record_deletion(self):
        user = User.objects.create_superuser(username='test19', email='test4@gmail.com', password='abc123def2')
        ngo = NGO.objects.create(user=user, ngo_name='Test NGO17', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user)
        ngo.delete()
        #Checking if date_voided is automatically set on record deletion
        self.assertIsNotNone(ngo.date_voided)

    
    def test_ngo_for_voided_to_be_true_on_deletion(self):
        user = User.objects.create_superuser(username='test20', email='test5@gmail.com', password='abc123def2')
        ngo = NGO.objects.create(user=user, ngo_name='Test NGO18', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user)
        ngo.delete()
        #Checking if voided is set True on record deletion
        self.assertTrue(ngo.voided)

    
    def test_ngo_for_voided_to_be_False_on_undeletion(self):
        user = User.objects.create_superuser(username='test21', email='test5@gmail.com', password='abc123def2')
        ngo = NGO.objects.create(user=user, ngo_name='Test NGO18', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user)
        ngo.delete()
        ngo.undelete()
        #Checking if voided is set False on record undeletion
        self.assertFalse(ngo.voided)

    
    def test_ngo_for_datevoided_to_be_None_on_undeletion(self):
        user = User.objects.create_superuser(username='test22', email='test5@gmail.com', password='abc123def2')
        ngo = NGO.objects.create(user=user, ngo_name='Test NGO18', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user)
        ngo.delete()
        ngo.undelete()
        #Checking if date_voided is set None on record undeletion
        self.assertIsNone(ngo.date_voided)


    def test_ngo_for_voidreason_to_be_None_on_undeletion(self):
        user = User.objects.create_superuser(username='test23', email='test5@gmail.com', password='abc123def2')
        ngo = NGO.objects.create(user=user, ngo_name='Test NGO18', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user)
        ngo.delete()
        ngo.undelete()
        #Checking if void_reason is set None on record undeletion
        self.assertIsNone(ngo.void_reason)

    
    def test_ngo_for_voidedby_to_be_None_on_undeletion(self):
        user = User.objects.create_superuser(username='test24', email='test5@gmail.com', password='abc123def2')
        ngo = NGO.objects.create(user=user, ngo_name='Test NGO18', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user)
        ngo.delete()
        ngo.undelete()
        #Checking if voided_by is set None on record undeletion
        self.assertIsNone(ngo.voided_by)

    
    def test_ngo_for_permanent_deletion_on_purge(self):
        user = User.objects.create_superuser(username='test25', email='test5@gmail.com', password='abc123def2')
        ngo = NGO.objects.create(user=user, ngo_name='Test NGO18', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user)
        ngo.purge()
        ngouuid = ngo.uuid    
        #Checking if ngo is deleted permanently
        self.assertIsNone(NGO.objects.filter(uuid=ngouuid).first())

    
    def test_one_ngo_per_user(self):
        user1 = User.objects.create_superuser(username='test26', email='test1@gmail.com', password='abc123def1')
        ngo1 = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1)
        #Checking if Exception is thrown on linking 2 NGOs with one user, error must be thrown
        with self.assertRaises(Exception):
            ngo2 = NGO.objects.create(user=user1, ngo_name='Test NGO20', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1)
            

class DonorTest(TestCase):

    def setUp(self):
        # Pre-requisites for the test        
        return super().setUp()
    

    def test_donor_for_correct_insertions(self):
        user = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        donor = Donor.objects.create(user=user, donor_name='Test Donor', donor_cnic='00409858949', created_by=user)
        #Checking if inserted data is same as provided
        self.assertEqual(donor.donor_name, 'Test Donor')
        self.assertEqual(donor.donor_cnic, '00409858949')        
        self.assertEqual(donor.user.username, 'test1')
        self.assertEqual(donor.created_by.username, 'test1')

    
    def test_donor_for_auto_datecreated_on_record_insertion(self):
        user = User.objects.create_superuser(username='test2', email='test2@gmail.com', password='abc123def2')
        donor = Donor.objects.create(user=user, donor_name='Test Donor', donor_cnic='00409858949', created_by=user)
        #Checking if date_created is automatically set on record insertion
        self.assertIsNotNone(donor.date_created)


    def test_donor_table_for_auto_createdby_on_insertion(self):
        user1 = User.objects.create_superuser(username='test3', email='test3@gmail.com', password='abc123def3')        
        donor = Donor.objects.create(user=user1, donor_name='Test Donor', donor_cnic='00409858949', created_by=user1)
        #Checking if created_by is automatically set on record insertion
        self.assertIsNotNone(donor.created_by)


    def test_donor_for_auto_uuid_on_record_insertion(self):
        user1 = User.objects.create_superuser(username='test4', email='test4@gmail.com', password='abc123def2')
        donor = Donor.objects.create(user=user1, donor_name='Test Donor', donor_cnic='00409858949', created_by=user1)
        #Checking if uuid is automatically set on record insertion
        self.assertIsNotNone(donor.uuid)


    def test_donor_table_for_required_fields_on_record_creation(self):
        user1 = User.objects.create_superuser(username='test7', email='test1@gmail.com', password='abc123def1')
        user2 = User.objects.create_superuser(username='test8', email='test2@gmail.com', password='abc123def1')        
        #Checking if Donor table allows insertion with required values = None, error must be thrown
        with self.assertRaises(ValueError):
            donor1 = Donor.objects.create(user=user1, donor_cnic='00409858949', created_by=user1)
            donor2 = Donor.objects.create(user=user2, donor_name='Test Donor', created_by=user2)       


    def test_donor_for_auto_datedupdated_on_record_updation(self):
        user1 = User.objects.create_superuser(username='test15', email='test2@gmail.com', password='abc123def2')
        donor = Donor.objects.create(user=user1, donor_name='Test Donor', donor_cnic='00409858949', created_by=user1)
        donor.donor_name = 'Test1'
        donor.update()
        #Checking if date_updated is automatically set on record updation
        self.assertIsNotNone(donor.date_updated)

    
    def test_donor_for_auto_updatedby_on_record_updation(self):
        user1 = User.objects.create_superuser(username='test16', email='test2@gmail.com', password='abc123def2')
        donor = Donor.objects.create(user=user1, donor_name='Test Donor', donor_cnic='00409858949', created_by=user1)
        donor.donor_name = 'Test1'
        donor.update()
        #Checking if updated_by is automatically set on record updation
        self.assertIsNotNone(donor.updated_by)    


    def test_donor_for_auto_voidedby_on_record_deletion(self):
        user1 = User.objects.create_superuser(username='test17', email='test2@gmail.com', password='abc123def2')
        donor = Donor.objects.create(user=user1, donor_name='Test Donor', donor_cnic='00409858949', created_by=user1)
        donor.delete()
        #Checking if voidedby is automatically set on record deletion
        self.assertIsNotNone(donor.voided_by)

    
    def test_donor_for_auto_voidreason_on_record_deletion(self):
        user1 = User.objects.create_superuser(username='test18', email='test3@gmail.com', password='abc123def2')
        donor = Donor.objects.create(user=user1, donor_name='Test Donor', donor_cnic='00409858949', created_by=user1)
        donor.delete()
        #Checking if void_reason is automatically set on record deletion
        self.assertIsNotNone(donor.void_reason)

    
    def test_donor_for_auto_datevoided_on_record_deletion(self):
        user1 = User.objects.create_superuser(username='test19', email='test4@gmail.com', password='abc123def2')
        donor = Donor.objects.create(user=user1, donor_name='Test Donor', donor_cnic='00409858949', created_by=user1)
        donor.delete()
        #Checking if date_voided is automatically set on record deletion
        self.assertIsNotNone(donor.date_voided)

    
    def test_donor_for_voided_to_be_true_on_deletion(self):
        user1 = User.objects.create_superuser(username='test20', email='test5@gmail.com', password='abc123def2')
        donor = Donor.objects.create(user=user1, donor_name='Test Donor', donor_cnic='00409858949', created_by=user1)
        donor.delete()
        #Checking if voided is set True on record deletion
        self.assertTrue(donor.voided) 


    def test_donor_for_voided_to_be_False_on_undeletion(self):
        user1 = User.objects.create_superuser(username='test21', email='test5@gmail.com', password='abc123def2')
        donor = Donor.objects.create(user=user1, donor_name='Test Donor', donor_cnic='00409858949', created_by=user1)
        donor.delete()
        donor.undelete()
        #Checking if voided is set False on record undeletion
        self.assertFalse(donor.voided)

    
    def test_donor_for_datevoided_to_be_None_on_undeletion(self):
        user1 = User.objects.create_superuser(username='test22', email='test5@gmail.com', password='abc123def2')
        donor = Donor.objects.create(user=user1, donor_name='Test Donor', donor_cnic='00409858949', created_by=user1)
        donor.delete()
        donor.undelete()
        #Checking if date_voided is set None on record undeletion
        self.assertIsNone(donor.date_voided)


    def test_donor_for_voidreason_to_be_None_on_undeletion(self):
        user1 = User.objects.create_superuser(username='test23', email='test5@gmail.com', password='abc123def2')
        donor = Donor.objects.create(user=user1, donor_name='Test Donor', donor_cnic='00409858949', created_by=user1)
        donor.delete()
        donor.undelete()
        #Checking if void_reason is set None on record undeletion
        self.assertIsNone(donor.void_reason)

    
    def test_donor_for_voidedby_to_be_None_on_undeletion(self):
        user1 = User.objects.create_superuser(username='test24', email='test5@gmail.com', password='abc123def2')
        donor = Donor.objects.create(user=user1, donor_name='Test Donor', donor_cnic='00409858949', created_by=user1)
        donor.delete()
        donor.undelete()
        #Checking if voided_by is set None on record undeletion
        self.assertIsNone(donor.voided_by)


    def test_donor_for_permanent_deletion_on_purge(self):
        user1 = User.objects.create_superuser(username='test25', email='test5@gmail.com', password='abc123def2')
        donor = Donor.objects.create(user=user1, donor_name='Test Donor', donor_cnic='00409858949', created_by=user1)
        donor.purge()
        donoruuid = donor.uuid    
        #Checking if Donor is deleted permanently
        self.assertIsNone(Donor.objects.filter(uuid=donoruuid).first())


    def test_one_donor_per_user(self):
        user1 = User.objects.create_superuser(username='test26', email='test1@gmail.com', password='abc123def1')
        donor = Donor.objects.create(user=user1, donor_name='Test Donor', donor_cnic='00409858949', created_by=user1)
        #Checking if Exception is thrown on linking 2 Donors with one user, error must be thrown
        with self.assertRaises(Exception):
            donor = Donor.objects.create(user=user1, donor_name='Test Donor 2', donor_cnic='004098589453', created_by=user1)


class CampaignTest(TestCase):

    def setUp(self):
        # Pre-requisites for the test        
        return super().setUp()
    

    def test_campaign_for_correct_insertions(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        campaign = Campaign.objects.create(campaign_name='Test Camp 1', campaign_description='Descrp 1', campaign_image='abc.jpg', 
                                           NGO=ngo, created_by=user1)
        #Checking if inserted data is same as provided
        self.assertEqual(campaign.campaign_name, 'Test Camp 1')
        self.assertEqual(campaign.campaign_description, 'Descrp 1') 
        self.assertEqual(campaign.campaign_image, 'abc.jpg')        
        self.assertEqual(campaign.NGO.ngo_name, 'Test NGO19')
        self.assertEqual(campaign.created_by.username, 'test1')

    
    def test_campaign_for_auto_datecreated_on_record_insertion(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        campaign = Campaign.objects.create(campaign_name='Test Camp 2', campaign_description='Descrp 1', campaign_image='abc.jpg', 
                                           NGO=ngo, created_by=user1)
        #Checking if date_created is automatically set on record insertion
        self.assertIsNotNone(campaign.date_created)


    def test_campaign_table_for_auto_createdby_on_insertion(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        campaign = Campaign.objects.create(campaign_name='Test Camp 3', campaign_description='Descrp 1', campaign_image='abc.jpg', 
                                           NGO=ngo, created_by=user1)
        #Checking if created_by is automatically set on record insertion
        self.assertIsNotNone(campaign.created_by)


    def test_campaign_for_auto_uuid_on_record_insertion(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        campaign = Campaign.objects.create(campaign_name='Test Camp 4', campaign_description='Descrp 1', campaign_image='abc.jpg', 
                                           NGO=ngo, created_by=user1)
        #Checking if uuid is automatically set on record insertion
        self.assertIsNotNone(campaign.uuid)

    
    def test_campaign_table_for_required_fields_on_record_creation(self):
        user1 = User.objects.create_superuser(username='test7', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1)         
        #Checking if Campaign table allows insertion with required values = None, error must be thrown
        with self.assertRaises(ValueError):
            Campaign.objects.create(campaign_description='Descrp 1', campaign_image='abc.jpg', 
                                    NGO=ngo, created_by=user1)     
            Campaign.objects.create(campaign_name='Test Camp 1', campaign_image='abc.jpg', 
                                    NGO=ngo, created_by=user1)  
            Campaign.objects.create(campaign_name='Test Camp 2', campaign_description='Descrp 1', 
                                    NGO=ngo, created_by=user1)
            Campaign.objects.create(campaign_name='Test Camp 3', campaign_description='Descrp 1', campaign_image='abc.jpg', 
                                    created_by=user1)


    def test_campaign_for_auto_datedupdated_on_record_updation(self):
        user1 = User.objects.create_superuser(username='test7', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        campaign = Campaign.objects.create(campaign_name='Test Camp 4', campaign_description='Descrp 1', campaign_image='abc.jpg', 
                                NGO=ngo, created_by=user1)
        campaign.campaign_name = 'Test1'
        campaign.update()
        #Checking if date_updated is automatically set on record updation
        self.assertIsNotNone(campaign.date_updated)

    
    def test_campaign_for_auto_updatedby_on_record_updation(self):
        user1 = User.objects.create_superuser(username='test7', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        campaign = Campaign.objects.create(campaign_name='Test Camp 4', campaign_description='Descrp 1', campaign_image='abc.jpg', 
                                NGO=ngo, created_by=user1)
        campaign.campaign_name = 'Test1'
        campaign.update()
        #Checking if updated_by is automatically set on record updation
        self.assertIsNotNone(campaign.updated_by)    


    def test_campaign_for_auto_voidedby_on_record_deletion(self):
        user1 = User.objects.create_superuser(username='test7', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        campaign = Campaign.objects.create(campaign_name='Test Camp 4', campaign_description='Descrp 1', campaign_image='abc.jpg', 
                                NGO=ngo, created_by=user1)
        campaign.delete()
        #Checking if voidedby is automatically set on record deletion
        self.assertIsNotNone(campaign.voided_by)

    
    def test_campaign_for_auto_voidreason_on_record_deletion(self):
        user1 = User.objects.create_superuser(username='test7', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        campaign = Campaign.objects.create(campaign_name='Test Camp 4', campaign_description='Descrp 1', campaign_image='abc.jpg', 
                                NGO=ngo, created_by=user1)
        campaign.delete()
        #Checking if void_reason is automatically set on record deletion
        self.assertIsNotNone(campaign.void_reason)

    
    def test_campaign_for_auto_datevoided_on_record_deletion(self):
        user1 = User.objects.create_superuser(username='test7', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        campaign = Campaign.objects.create(campaign_name='Test Camp 4', campaign_description='Descrp 1', campaign_image='abc.jpg', 
                                NGO=ngo, created_by=user1)
        campaign.delete()
        #Checking if date_voided is automatically set on record deletion
        self.assertIsNotNone(campaign.date_voided)

    
    def test_campaign_for_voided_to_be_true_on_deletion(self):
        user1 = User.objects.create_superuser(username='test7', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        campaign = Campaign.objects.create(campaign_name='Test Camp 4', campaign_description='Descrp 1', campaign_image='abc.jpg', 
                                NGO=ngo, created_by=user1)
        campaign.delete()
        #Checking if voided is set True on record deletion
        self.assertTrue(campaign.voided)
    

    def test_campaign_for_voided_to_be_False_on_undeletion(self):
        user1 = User.objects.create_superuser(username='test7', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        campaign = Campaign.objects.create(campaign_name='Test Camp 4', campaign_description='Descrp 1', campaign_image='abc.jpg', 
                                NGO=ngo, created_by=user1)
        campaign.delete()
        campaign.undelete()
        #Checking if voided is set False on record undeletion
        self.assertFalse(campaign.voided)

    
    def test_campaign_for_datevoided_to_be_None_on_undeletion(self):
        user1 = User.objects.create_superuser(username='test7', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        campaign = Campaign.objects.create(campaign_name='Test Camp 4', campaign_description='Descrp 1', campaign_image='abc.jpg', 
                                NGO=ngo, created_by=user1)
        campaign.delete()
        campaign.undelete()
        #Checking if date_voided is set None on record undeletion
        self.assertIsNone(campaign.date_voided)


    def test_campaign_for_voidreason_to_be_None_on_undeletion(self):
        user1 = User.objects.create_superuser(username='test7', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        campaign = Campaign.objects.create(campaign_name='Test Camp 4', campaign_description='Descrp 1', campaign_image='abc.jpg', 
                                NGO=ngo, created_by=user1)
        campaign.delete()
        campaign.undelete()
        #Checking if void_reason is set None on record undeletion
        self.assertIsNone(campaign.void_reason)

    
    def test_campaign_for_voidedby_to_be_None_on_undeletion(self):
        user1 = User.objects.create_superuser(username='test7', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        campaign = Campaign.objects.create(campaign_name='Test Camp 4', campaign_description='Descrp 1', campaign_image='abc.jpg', 
                                NGO=ngo, created_by=user1)
        campaign.delete()
        campaign.undelete()
        #Checking if voided_by is set None on record undeletion
        self.assertIsNone(campaign.voided_by)


    def test_campaign_for_permanent_deletion_on_purge(self):
        user1 = User.objects.create_superuser(username='test7', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        campaign = Campaign.objects.create(campaign_name='Test Camp 4', campaign_description='Descrp 1', campaign_image='abc.jpg', 
                                NGO=ngo, created_by=user1)
        campaignuuid = campaign.uuid
        campaign.purge()
        #Checking if Campaign is deleted permanently
        self.assertIsNone(Campaign.objects.filter(uuid=campaignuuid).first())


class SponsorRequestTest(TestCase):

    def setUp(self):
        # Pre-requisites for the test        
        return super().setUp()
    

    def test_sponsorrequests_for_correct_insertions(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        #Checking if inserted data is same as provided
        self.assertEqual(request.request_name, 'Test Name 1')
        self.assertEqual(request.request_description, 'Descrp 1') 
        self.assertEqual(request.request_image, 'abc.jpg')   
        self.assertEqual(request.request_price, 400)        
        self.assertEqual(request.NGO.ngo_name, 'Test NGO19')
        self.assertEqual(request.created_by.username, 'test1')


    def test_sponsorrequests_for_auto_datecreated_on_record_insertion(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        #Checking if date_created is automatically set on record insertion
        self.assertIsNotNone(request.date_created)


    def test_sponsorrequests_for_auto_createdby_on_insertion(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        #Checking if created_by is automatically set on record insertion
        self.assertIsNotNone(request.created_by)


    def test_sponsorrequests_for_auto_uuid_on_record_insertion(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        #Checking if uuid is automatically set on record insertion
        self.assertIsNotNone(request.uuid)

    
    def test_sponsorrequests_table_for_required_fields_on_record_creation(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1)     
        #Checking if SponsorRequests table allows insertion with required values = None, error must be thrown
        with self.assertRaises(ValueError):
            SponsorRequest.objects.create(request_description='Descrp 1', request_image='abc.jpg',
                                            request_price=400, NGO=ngo)
            SponsorRequest.objects.create(request_name='Test Name 1', request_image='abc.jpg',
                                            request_price=400, NGO=ngo)  
            SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1',
                                            request_price=400, NGO=ngo)
            SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                            NGO=ngo)
            SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                            request_price=400) 
    

    def test_sponsorrequests_for_auto_datedupdated_on_record_updation(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        request.request_name = 'Test1'
        request.update()
        #Checking if date_updated is automatically set on record updation
        self.assertIsNotNone(request.date_updated)

    
    def test_sponsorrequests_for_auto_updatedby_on_record_updation(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        request.request_name = 'Test1'
        request.update()
        #Checking if updated_by is automatically set on record updation
        self.assertIsNotNone(request.updated_by)
    

    def test_sponsorrequests_for_auto_voidedby_on_record_deletion(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        request.delete()
        #Checking if voidedby is automatically set on record deletion
        self.assertIsNotNone(request.voided_by)

    
    def test_sponsorrequests_for_auto_voidreason_on_record_deletion(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        request.delete()
        #Checking if void_reason is automatically set on record deletion
        self.assertIsNotNone(request.void_reason)

    
    def test_sponsorrequests_for_auto_datevoided_on_record_deletion(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        request.delete()
        #Checking if date_voided is automatically set on record deletion
        self.assertIsNotNone(request.date_voided)

    
    def test_sponsorrequests_for_voided_to_be_true_on_deletion(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        request.delete()
        #Checking if voided is set True on record deletion
        self.assertTrue(request.voided)
    

    def test_sponsorrequests_for_voided_to_be_False_on_undeletion(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        request.delete()
        request.undelete()
        #Checking if voided is set False on record undeletion
        self.assertFalse(request.voided)

    
    def test_sponsorrequests_for_datevoided_to_be_None_on_undeletion(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        request.delete()
        request.undelete()
        #Checking if date_voided is set None on record undeletion
        self.assertIsNone(request.date_voided)


    def test_sponsorrequests_for_voidreason_to_be_None_on_undeletion(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        request.delete()
        request.undelete()
        #Checking if void_reason is set None on record undeletion
        self.assertIsNone(request.void_reason)

    
    def test_sponsorrequests_for_voidedby_to_be_None_on_undeletion(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        request.delete()
        request.undelete()
        #Checking if voided_by is set None on record undeletion
        self.assertIsNone(request.voided_by)


    def test_sponsorrequests_for_permanent_deletion_on_purge(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        requestuuid = request.uuid
        request.purge()
        #Checking if SponsorRequests is deleted permanently
        self.assertIsNone(Campaign.objects.filter(uuid=requestuuid).first())


class DonationTest(TestCase):

    def setUp(self):
        # Pre-requisites for the test        
        return super().setUp()
    

    def test_donations_for_correct_insertions(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        user2 = User.objects.create_superuser(username='test2', email='test2@gmail.com', password='abc123def2')
        donor = Donor.objects.create(user=user2, donor_name='Test Donor', donor_cnic='00409858949', created_by=user2)
        donation = Donation.objects.create(SponsorRequest=request, Donor=donor)
        #Checking if inserted data is same as provided
        self.assertEqual(donation.SponsorRequest.request_name, 'Test Name 1')
        self.assertEqual(donation.Donor.donor_name, 'Test Donor')


    def test_donations_for_auto_datecreated_on_record_insertion(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        user2 = User.objects.create_superuser(username='test2', email='test2@gmail.com', password='abc123def2')
        donor = Donor.objects.create(user=user2, donor_name='Test Donor', donor_cnic='00409858949', created_by=user2)
        donation = Donation.objects.create(SponsorRequest=request, Donor=donor)
        #Checking if date_created is automatically set on record insertion
        self.assertIsNotNone(donation.date_created)


    def test_donations_table_for_auto_createdby_on_insertion(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        user2 = User.objects.create_superuser(username='test2', email='test2@gmail.com', password='abc123def2')
        donor = Donor.objects.create(user=user2, donor_name='Test Donor', donor_cnic='00409858949', created_by=user2)
        donation = Donation.objects.create(SponsorRequest=request, Donor=donor)
        #Checking if created_by is automatically set on record insertion
        self.assertIsNotNone(donation.created_by)


    def test_donations_for_auto_uuid_on_record_insertion(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        user2 = User.objects.create_superuser(username='test2', email='test2@gmail.com', password='abc123def2')
        donor = Donor.objects.create(user=user2, donor_name='Test Donor', donor_cnic='00409858949', created_by=user2)
        donation = Donation.objects.create(SponsorRequest=request, Donor=donor)
        #Checking if uuid is automatically set on record insertion
        self.assertIsNotNone(donation.uuid)
    

    def test_donations_for_auto_datedupdated_on_record_updation(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        user2 = User.objects.create_superuser(username='test2', email='test2@gmail.com', password='abc123def2')
        user3 = User.objects.create_superuser(username='test3', email='test3@gmail.com', password='abc123def2')
        donor1 = Donor.objects.create(user=user2, donor_name='Test Donor', donor_cnic='00409858949', created_by=user2)
        donor2 = Donor.objects.create(user=user3, donor_name='Test Donor 2', donor_cnic='00409858949', created_by=user3)
        donation = Donation.objects.create(SponsorRequest=request, Donor=donor1) 
        donation.Donor = donor2
        donation.update()
        #Checking if date_updated is automatically set on record updation
        self.assertIsNotNone(donation.date_updated)

    
    def test_donations_for_auto_updatedby_on_record_updation(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        user2 = User.objects.create_superuser(username='test2', email='test2@gmail.com', password='abc123def2')
        user3 = User.objects.create_superuser(username='test3', email='test3@gmail.com', password='abc123def2')
        donor1 = Donor.objects.create(user=user2, donor_name='Test Donor', donor_cnic='00409858949', created_by=user2)
        donor2 = Donor.objects.create(user=user3, donor_name='Test Donor 2', donor_cnic='00409858949', created_by=user3)
        donation = Donation.objects.create(SponsorRequest=request, Donor=donor1) 
        donation.Donor = donor2
        donation.update()
        #Checking if updated_by is automatically set on record updation
        self.assertIsNotNone(donation.updated_by)
    

    def test_donations_for_auto_voidedby_on_record_deletion(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        user2 = User.objects.create_superuser(username='test2', email='test2@gmail.com', password='abc123def2')
        donor = Donor.objects.create(user=user2, donor_name='Test Donor', donor_cnic='00409858949', created_by=user2)
        donation = Donation.objects.create(SponsorRequest=request, Donor=donor)
        donation.delete()
        #Checking if voidedby is automatically set on record deletion
        self.assertIsNotNone(donation.voided_by)

    
    def test_donations_for_auto_voidreason_on_record_deletion(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        user2 = User.objects.create_superuser(username='test2', email='test2@gmail.com', password='abc123def2')
        donor = Donor.objects.create(user=user2, donor_name='Test Donor', donor_cnic='00409858949', created_by=user2)
        donation = Donation.objects.create(SponsorRequest=request, Donor=donor)
        donation.delete()
        #Checking if void_reason is automatically set on record deletion
        self.assertIsNotNone(donation.void_reason)

    
    def test_donations_for_auto_datevoided_on_record_deletion(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        user2 = User.objects.create_superuser(username='test2', email='test2@gmail.com', password='abc123def2')
        donor = Donor.objects.create(user=user2, donor_name='Test Donor', donor_cnic='00409858949', created_by=user2)
        donation = Donation.objects.create(SponsorRequest=request, Donor=donor)
        donation.delete()
        #Checking if date_voided is automatically set on record deletion
        self.assertIsNotNone(donation.date_voided)

    
    def test_donations_for_voided_to_be_true_on_deletion(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        user2 = User.objects.create_superuser(username='test2', email='test2@gmail.com', password='abc123def2')
        donor = Donor.objects.create(user=user2, donor_name='Test Donor', donor_cnic='00409858949', created_by=user2)
        donation = Donation.objects.create(SponsorRequest=request, Donor=donor)
        donation.delete()
        #Checking if voided is set True on record deletion
        self.assertTrue(donation.voided)
    

    def test_donations_for_voided_to_be_False_on_undeletion(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        user2 = User.objects.create_superuser(username='test2', email='test2@gmail.com', password='abc123def2')
        donor = Donor.objects.create(user=user2, donor_name='Test Donor', donor_cnic='00409858949', created_by=user2)
        donation = Donation.objects.create(SponsorRequest=request, Donor=donor)
        donation.delete()
        donation.undelete()
        #Checking if voided is set False on record undeletion
        self.assertFalse(donation.voided)

    
    def test_donations_for_datevoided_to_be_None_on_undeletion(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        user2 = User.objects.create_superuser(username='test2', email='test2@gmail.com', password='abc123def2')
        donor = Donor.objects.create(user=user2, donor_name='Test Donor', donor_cnic='00409858949', created_by=user2)
        donation = Donation.objects.create(SponsorRequest=request, Donor=donor)
        donation.delete()
        donation.undelete()
        #Checking if date_voided is set None on record undeletion
        self.assertIsNone(donation.date_voided)


    def test_donations_for_voidreason_to_be_None_on_undeletion(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        user2 = User.objects.create_superuser(username='test2', email='test2@gmail.com', password='abc123def2')
        donor = Donor.objects.create(user=user2, donor_name='Test Donor', donor_cnic='00409858949', created_by=user2)
        donation = Donation.objects.create(SponsorRequest=request, Donor=donor)
        donation.delete()
        donation.undelete()
        #Checking if void_reason is set None on record undeletion
        self.assertIsNone(donation.void_reason)

    
    def test_donations_for_voidedby_to_be_None_on_undeletion(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        user2 = User.objects.create_superuser(username='test2', email='test2@gmail.com', password='abc123def2')
        donor = Donor.objects.create(user=user2, donor_name='Test Donor', donor_cnic='00409858949', created_by=user2)
        donation = Donation.objects.create(SponsorRequest=request, Donor=donor)
        donation.delete()
        donation.undelete()
        #Checking if voided_by is set None on record undeletion
        self.assertIsNone(donation.voided_by)
    

    def test_donation_for_permanent_deletion_on_purge(self):
        user1 = User.objects.create_superuser(username='test1', email='test1@gmail.com', password='abc123def1')
        ngo = NGO.objects.create(user=user1, ngo_name='Test NGO19', ngo_address='Test Address', ngo_description='Test Description', 
                                 ngo_phone='1234567890', ngo_bank_name='Test Bank', ngo_account_title='Test Account', ngo_account_no='123456789', 
                                 ngo_image='test_image.jpg', created_by=user1) 
        request = SponsorRequest.objects.create(request_name='Test Name 1', request_description='Descrp 1', request_image='abc.jpg',
                                                request_price=400, NGO=ngo)
        user2 = User.objects.create_superuser(username='test2', email='test2@gmail.com', password='abc123def2')
        donor = Donor.objects.create(user=user2, donor_name='Test Donor', donor_cnic='00409858949', created_by=user2)
        donation = Donation.objects.create(SponsorRequest=request, Donor=donor)
        donationuuid = donation.uuid
        donation.purge()
        #Checking if Donation is deleted permanently
        self.assertIsNone(Donation.objects.filter(uuid=donationuuid).first())
            
    
        
        
            

        
        
        


    
