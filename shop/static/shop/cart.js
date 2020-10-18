if($('#totalPrice').length>0)
{
    document.getElementById('totalPrice').innerText = '\u20B9'+localStorage.getItem('carttotal')
}
let uname=sessionStorage.getItem('uname')
if(uname!=null && uname!='Login')
{
    document.getElementById('uname3').value = uname
}
function clearCart()
{
    let clearcartconfirm = confirm('Are you sure you want to clear your cart? ')
    if(clearcartconfirm)
        localStorage.clear() 
    alert('Cart emptied successfully')
    location.href = '/shop'
}
