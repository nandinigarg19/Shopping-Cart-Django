function countItems(cart)
{
    let sum=0
    let carttotal = 0
    for(let item in cart)
    {
        sum+=cart[item]['qty']
        carttotal+=(cart[item]['price']*cart[item]['qty'])
    }
    console.log(sum)
    console.log(carttotal)
    localStorage.setItem('carttotal',carttotal)
    return sum
}

if(localStorage.getItem('cart') == null)
{
    var cart={}
}
else
{
    cart = JSON.parse(localStorage.getItem('cart'))
}

document.getElementById('cartitemcountvalue').innerHTML = countItems(cart)

