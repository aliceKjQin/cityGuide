// Fill stars on mouseover
const starContainer = document.querySelector('#star-container')
const stars = [...starContainer.querySelectorAll('.star')]

stars.forEach((star, index) => {
    star.addEventListener('mouseover', () =>{
        stars.forEach((s, i) => {
            if (i <= index) {
                s.classList.add('filled');
            } else {
                s.classList.remove('filled')
            }
        })
    })
})