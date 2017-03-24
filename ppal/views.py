from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PaypalPaymentsForm

def home(request)
	args = {}

	paypal_dict = {
		"business" : "magical.singhal@gmail.com" ,
		"amount" : "100.00" ,
		"currency_code" : "IND" ,
		"item_name" : "Community" ,
		"notify_url" : "http://a-guess/",
		"return_url" : "http://paypal-return",
		"cancel_url" : "http://paypal-cancle",

	}

	form = PaypalPaymentsForm(initail=paypal_dict)
	args['form'] = form
	return render_to_response('home.html', args)

def paypal_return(request):
	args = {'post' : request.POST, 'get': request.GET}
	return render_to_response('paypal_return.html', args)

def paypal_cancel(request):
	args = {'post': request.POST, 'get':request.GET}
	return render_to_response('paypal_cancel.html', args)
