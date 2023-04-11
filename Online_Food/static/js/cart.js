var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var fooditem_id = this.dataset.fooditem
		var action = this.dataset.action
		console.log('fooditem_id:', fooditem_id, 'Action:', action)
		console.log('USER:', user)

		if (user == 'AnonymousUser'){
			addCookieItem(fooditem_id, action)

		}else{
			updateUserOrder(fooditem_id, action)
		}
	})
}

function updateUserOrder(fooditem_id, action){
     console.log('User is Authenticated, Sending data..')

        var url = '/update_item/'

        fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			},
            body:JSON.stringify({'fooditem_id':fooditem_id, 'action':action})
        })

        .then((response) => {
		   return response.json();
		})
		.then((data) => {
		    location.reload()
		});
}

