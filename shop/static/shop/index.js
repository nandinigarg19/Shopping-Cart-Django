if(localStorage.getItem('cart') == null)
{
    var cart={}
    document.getElementById('cartitemcountvalue').innerHTML = 0
}
else
{
    cart = JSON.parse(localStorage.getItem('cart'))
    document.getElementById('cartitemcountvalue').innerHTML = countItems(cart)
}

$(document).ready(function(){
    console.log(cart)
    for(let i in cart)
    {
        document.querySelector('div#atc'+i+' button').click()
        document.querySelector('button#minus'+i).click()
    }
    // let uname = document.getElementById('loginbutton_id').innerText
    // document.getElementById('uname1').value = uname
    // document.getElementById('uname2').value = uname  
})

$('.cartshow').on("submit","form.cartform",async function(){
    document.getElementById('itemsJson').setAttribute('value',JSON.stringify(cart))
})

$('.atcbuttonouter').on("click","button.atcbutton",async function(){
    var idstr = this.id.toString();
    if(cart[idstr] != undefined)
        cart[idstr]['qty'] += 1
    else    
    {
        var product = {}
        product['qty'] = 1
        product['name'] = document.getElementById('name'+idstr).innerText
        product['img'] = document.getElementById('image'+idstr).getAttribute('src')
        product['price'] = document.getElementById('price'+idstr).innerText
        cart[idstr] = product
    }
    localStorage.setItem('cart',JSON.stringify(cart))
    
    document.getElementById('cartitemcountvalue').innerHTML = countItems(cart)
    document.getElementById('atc'+idstr).innerHTML = `
        <button class="btn btn-primary minusbutton ml-5" id="minus${idstr}" style="width: 30px; height: 30px; padding: -0.625rem">-</button>
        <input type="text" value="${cart[idstr]['qty']}" id = "count${idstr}" style="width:30px; text-align: center" disabled>
        <button class="btn btn-primary plusbutton" id="plus${idstr}" style="width: 30px; height: 30px; padding: -0.625rem">+</button>          
    `
})

$('.atcbuttonouter').on("click","button.plusbutton",function(){
    var idstr = this.id.toString().slice(4);
    if(cart[idstr]['qty']>=9)
        alert('You can not add more than 9 quantities of same product')
    else
    {
        cart[idstr]['qty'] += 1
        localStorage.setItem('cart',JSON.stringify(cart))
        document.getElementById('cartitemcountvalue').innerHTML = countItems(cart)
        document.getElementById('count'+idstr).setAttribute('value',cart[idstr]['qty'])
    }
})

$('.atcbuttonouter').on("click","button.minusbutton",function(){
    var idstr = this.id.toString().slice(5);
    if(cart[idstr]['qty']==1)
    {
        document.getElementById('atc'+idstr).innerHTML = `
            <button class="btn btn-primary atcbutton ml-5" id="${idstr}">Add to cart</button>
        `
        delete cart[idstr]
        localStorage.setItem('cart',JSON.stringify(cart))
        location.reload(true)
    }
    else
    {
        cart[idstr]['qty'] -= 1
        localStorage.setItem('cart',JSON.stringify(cart))
        document.getElementById('cartitemcountvalue').innerHTML = countItems(cart)
        document.getElementById('count'+idstr).setAttribute('value',cart[idstr]['qty'])
    }
})



