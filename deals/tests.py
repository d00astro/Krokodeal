from django.test import TestCase

from deals.models import Deal
from deals.models import Profile
from django.contrib.auth.models import User

class DealMethodTests(TestCase):

    def test_unique_vote_up(self):
        """
        A user vote on a deal should raise the temperature
        """
        
        #Preparation
        myDeal = Deal()
        myDeal.title_text = "This is a fake product only for testing purposes"
        myDeal.link_url = "http://www.amazon.com"
        myDeal.vendor_text = "Amazon"
        myDeal.price_decimal = 10.3
        myDeal.description_text = "Lorem Ipsum Dolor sit amet esperum funcionorum perfectunum"
        myDeal.imageUrl_url = "http://www.amazon.com"
        myDeal.save()
                    
        myUser = User()
        myUser.username = "jonh.doe"
        myUser.save()
        
        myProfile = Profile()
        myProfile.user = myUser
        myProfile.save()
    
        currentVotes = myDeal.temperature
    
        #Action
        voteOutput = myDeal.upvote(myUser.id)
    
        #Review
        self.assertEqual(voteOutput, True)
        self.assertEqual((currentVotes < myDeal.temperature), True)

    def test_repeated_vote_up(self):
        """
        A user should be able to vote up, only if he has never voted before on the same article
        """
        
        #Preparation
        myDeal = Deal()
        myDeal.title_text = "This is a fake product only for testing purposes"
        myDeal.link_url = "http://www.amazon.com"
        myDeal.vendor_text = "Amazon"
        myDeal.price_decimal = 10.3
        myDeal.description_text = "Lorem Ipsum Dolor sit amet esperum funcionorum perfectunum"
        myDeal.imageUrl_url = "http://www.amazon.com"
        myDeal.save()
                    
        myUser = User()
        myUser.username = "jonh.doe"
        myUser.save()
        
        myProfile = Profile()
        myProfile.user = myUser
        myProfile.save()
        
        myDeal.upvote(myUser.id)
    
        currentVotes = myDeal.temperature
    
        #Action
        voteOutput = myDeal.upvote(myUser)
    
        #Review
        self.assertEqual(voteOutput, False)
        self.assertEqual(currentVotes, myDeal.temperature)
        
    def test_unvote_vote_up(self):
        """
        If a user that has upvoted a deal downvotes it, he should be able to vote again
        """
        
        #Preparation
        myDeal = Deal()
        myDeal.title_text = "This is a fake product only for testing purposes"
        myDeal.link_url = "http://www.amazon.com"
        myDeal.vendor_text = "Amazon"
        myDeal.price_decimal = 10.3
        myDeal.description_text = "Lorem Ipsum Dolor sit amet esperum funcionorum perfectunum"
        myDeal.imageUrl_url = "http://www.amazon.com"
        myDeal.save()
                    
        myUser = User()
        myUser.username = "jonh.doe"
        myUser.save()
        
        myProfile = Profile()
        myProfile.user = myUser
        myProfile.save()
        
        myDeal.upvote(myUser.id)
        myDeal.downvote(myUser.id)
    
        currentVotes = myDeal.temperature
    
        #Action
        voteOutput = myDeal.upvote(myUser)
    
        #Review
        self.assertEqual(voteOutput, True)
        self.assertEqual((currentVotes < myDeal.temperature), True)
        
    def test_unique_vote_down(self):
        """
        A user should be able to vote down and decrease the temperature of the deal
        """
        
        #Preparation
        myDeal = Deal()
        myDeal.title_text = "This is a fake product only for testing purposes"
        myDeal.link_url = "http://www.amazon.com"
        myDeal.vendor_text = "Amazon"
        myDeal.price_decimal = 10.3
        myDeal.description_text = "Lorem Ipsum Dolor sit amet esperum funcionorum perfectunum"
        myDeal.imageUrl_url = "http://www.amazon.com"
        myDeal.save()
                    
        myUser = User()
        myUser.username = "jonh.doe"
        myUser.save()
        
        myProfile = Profile()
        myProfile.user = myUser
        myProfile.save()
    
        currentVotes = myDeal.temperature
    
        #Action
        voteOutput = myDeal.downvote(myUser)
    
        #Review
        self.assertEqual(voteOutput, True)
        self.assertEqual((currentVotes > myDeal.temperature), True)
        
    def test_repeated_vote_down(self):
        """
        A user should not be able to vote down, if he has already downvoted on an article
        """
        
        #Preparation
        myDeal = Deal()
        myDeal.title_text = "This is a fake product only for testing purposes"
        myDeal.link_url = "http://www.amazon.com"
        myDeal.vendor_text = "Amazon"
        myDeal.price_decimal = 10.3
        myDeal.description_text = "Lorem Ipsum Dolor sit amet esperum funcionorum perfectunum"
        myDeal.imageUrl_url = "http://www.amazon.com"
        myDeal.save()
                    
        myUser = User()
        myUser.username = "jonh.doe"
        myUser.save()
        
        myProfile = Profile()
        myProfile.user = myUser
        myProfile.save()
        
        myDeal.downvote(myUser)
    
        currentVotes = myDeal.temperature
        
        #Action
        voteOutput = myDeal.downvote(myUser)
    
        #Review
        self.assertEqual(voteOutput, False)
        self.assertEqual(currentVotes, myDeal.temperature)
        
    def test_unvote_vote_down(self):
        """
        If a user that has downvoted a deal upvotes it, he should be able to vote again
        """
        
        #Preparation
        myDeal = Deal()
        myDeal.title_text = "This is a fake product only for testing purposes"
        myDeal.link_url = "http://www.amazon.com"
        myDeal.vendor_text = "Amazon"
        myDeal.price_decimal = 10.3
        myDeal.description_text = "Lorem Ipsum Dolor sit amet esperum funcionorum perfectunum"
        myDeal.imageUrl_url = "http://www.amazon.com"
        myDeal.save()
        
        myUser = User()
        myUser.username = "jonh.doe"
        myUser.save()
        
        myProfile = Profile()
        myProfile.user = myUser
        myProfile.save()
        
        myDeal.downvote(myUser.id)
        myDeal.upvote(myUser.id)
    
        currentVotes = myDeal.temperature
    
        #Action
        voteOutput = myDeal.downvote(myUser)
    
        #Review
        self.assertEqual(voteOutput, True)
        self.assertEqual((currentVotes > myDeal.temperature), True)