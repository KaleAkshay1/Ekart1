// color buttons code for changing images in cart

const cart = document.querySelectorAll('.custom-card1')
console.log(cart)
Array.from(cart).forEach((element) => {
    const mimage = element.getElementsByClassName('m-image')[0]
    console.log(mimage)
    const cBtn = element.querySelectorAll('.c-button')
    console.log(cBtn)

    Array.from(cBtn).forEach((btn) => {
        btn.addEventListener('click', () => {
            const newSrc = btn.getAttribute('data-image')
            console.log(newSrc)
            mimage.src = newSrc
        })
    })
})

// dropdown menue for brand
const select = document.querySelector('.select')
const options1 = document.querySelector('.options')
const option = document.querySelectorAll('.option')
const sText = document.querySelector('.select-text')
const arrow = document.getElementById('arrow')

if (select) {
    select.addEventListener('click', () => {
        options1.classList.toggle('hide')
        arrow.classList.toggle('rotate')
    })
}
Array.from(option).forEach((element) => {
    element.addEventListener('click', () => {
        let text = element.querySelector('h5').textContent
        // sText.innerText = text
        // options.classList.add('hide')
        // arrow.classList.remove('rotate')
    })
})


// code for deetails image options
const mainImage = document.querySelector('.img-detail')
const imgOptions = document.querySelectorAll('.img-options')


Array.from(imgOptions).forEach((element) => {
    element.addEventListener('click', () => {
        let nSrc = element.getAttribute('data-image')
        mainImage.src = nSrc
    })
})





// code for detail color button

const cDetail = document.querySelectorAll('.color-detail')
const selectedColorInput = document.getElementById('selectedColor');

Array.from(cDetail).forEach((element) => {
    element.addEventListener('click', () => {


        let mImg1 = document.querySelector('.img-option1')
        let mImg2 = document.querySelector('.img-option2')
        let mImg3 = document.querySelector('.img-option3')

        let color = element.getAttribute('data-color')
        // console.log(color)



        let nImg1 = element.getAttribute('data-c-image1')
        let nImg2 = element.getAttribute('data-c-image2')
        let nImg3 = element.getAttribute('data-c-image3')

        mImg1.src = nImg1
        mImg2.src = nImg2
        mImg3.src = nImg3


        let img = document.querySelector('.img-detail')
        img.src = nImg1


        imgOptions.forEach((element, index) => {
            if (index == 0) {
                element.setAttribute('data-image', nImg1);
            } else if (index == 1) {
                element.setAttribute('data-image', nImg2);
            } else if (index == 2) {
                element.setAttribute('data-image', nImg3);
            }
        });


        let aCart = document.getElementsByClassName('add-to-cart')[0]
        if (aCart) {
            // console.log(aCart)
            let hLink = element.getAttribute('data-addCartBtn')
            // console.log(hLink)
            aCart.href = hLink
        }
    })
})

// profile code

let profile = document.getElementById('profile')
if(profile){
    profile.addEventListener('click',function(){
        let profiles = document.getElementsByClassName('profile')[0]
        profiles.classList.toggle('hide')
    })
}


// size form submition
// let sForm = document.getElementById('size-form');

// function submitForm() {
//     sForm.submit()
// }

//cart Modify
// let cModify = document.querySelectorAll('.modifyCart')
// if(cModify){
//     Array.from(cModify).forEach((element)=>{
//         element.addEventListener('click',{

//         })
//     })
// }

// login form validation
let uname = document.getElementById('username')
let password = document.getElementById('password')
let password2 = document.getElementById('password2')
let passError = document.getElementsByClassName('pass-error')[0]
let passError2 = document.getElementsByClassName('pass-error2')[0]

let uPassFunction = (password1,msg) =>{
    password1.addEventListener('input',function(){
        if(password1.value.length < 8 || password1.value.length > 12){
            msg.classList.remove('hide')
        }else{
            msg.classList.add('hide')
        }
    })
}
if(password){
    uPassFunction(password,passError)
}
if(password2){
    uPassFunction(password2,passError2)
}
let uPassFunction2= (pass1,pass2,msg) =>{
    pass2.addEventListener('input',function(){
        if(pass1.value !== pass2.value){
            msg.innerText = 'Password and conform password is not same'
            msg.classList.remove('hide')
        }else{
            msg.innerText = 'Password must have 8 to 12 Charecter'
            msg.classList.add('hide')
        }
    })
}

if(password && password2){
    uPassFunction2(password,password2,passError2)
}