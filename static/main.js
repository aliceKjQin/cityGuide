// js for star rating

const starContainer = document.querySelector('#star-container')
const stars = starContainer.querySelectorAll('.star')
let selectedRating = 0
//Fill stars on mouseover
stars.forEach((star, index) => {
    star.addEventListener('mouseover', () =>{
        selectedRating = index + 1 
        stars.forEach((s, i) => {
            if (i <= index) {
                s.classList.add('filled');
            } else {
                s.classList.remove('filled')
            }
        })    
    })
})
//Capture the form submission and set the hidden input value
const form = document.querySelector('#rating-form')
form.addEventListener('submit', () => {
const hiddenInput = document.createElement('input')
hiddenInput.type = 'hidden'
hiddenInput.name = 'star_rating'
hiddenInput.value = selectedRating
form.appendChild(hiddenInput)
})
