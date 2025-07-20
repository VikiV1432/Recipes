function createOptions(items) {
    const optionsDiv = document.createElement('div')
    optionsDiv.classList.add('options')
    const optionsHeader = document.createElement('div')
    optionsHeader.classList.add('options__chosen')
    const optionsChosenText = document.createElement('p')
    optionsChosenText.classList.add('options__chosen-text')
    optionsChosenText.textContent = 'Not Chosen'
    const arrowDown = document.createElement('img')
    arrowDown.src = '/static/main/images/down-arrow.png'
    arrowDown.alt = 'down arrow'
    optionsHeader.appendChild(optionsChosenText)
    optionsHeader.appendChild(arrowDown)
    const optionsContent = document.createElement('div')
    optionsContent.classList.add('options__content')
    const optionsSearch = document.createElement('div')
    optionsSearch.classList.add('options__search')
    const input = document.createElement('input')
    input.type = 'text'
    input.placeholder = 'search'
    input.classList.add('field')
    optionsSearch.appendChild(input)
    optionsContent.appendChild(optionsSearch)
    const optionsItems = document.createElement('div')
    optionsItems.classList.add('options__items')
    const optionsItemList = []

    items.forEach((item) => {
        const optionsItem = document.createElement('div')
        optionsItem.classList.add('options__item')
        if (item.image) {
            const optionsItemImage = document.createElement('img')
            optionsItemImage.src = item.image
            optionsItem.appendChild(optionsItemImage)
        }
        optionsItem.textContent = item.title
        optionsItems.appendChild(optionsItem)
        optionsItemList.push(optionsItem)
    })
    optionsContent.appendChild(optionsItems)
    optionsDiv.appendChild(optionsHeader)
    optionsDiv.appendChild(optionsContent)
    


    optionsHeader.addEventListener('click', (e) => {
        const options = document.querySelectorAll('.options')
        for (const opt of options) {
            if(opt !== optionsDiv) {
                opt.classList.remove('open')
            }
        }
        optionsDiv.classList.toggle('open')
        optionsSearch.focus()
    })


    optionsItems.addEventListener('click', (e) => {
        const target = e.target
        if (target.classList.contains('options__item')) {
            optionsDiv.classList.remove('open')
            optionsChosenText.textContent = target.textContent
        }
    })

    optionsSearch.addEventListener('input', (e) => {
        const text = e.target.value
        const foundItems = items.filter((item) => item.title.toLowerCase().includes(text.toLowerCase()))
        optionsItems.innerHTML = ''
        for (const item of foundItems) {
            const div = document.createElement('div')
            div.classList.add('options__item')
            div.textContent = item.title
            optionsItems.appendChild(div)
        }
    })
    return optionsDiv
}

async function getIngredientsAndUnits(){
    const response=await fetch('/api/ingredients')
    const data=await response.json()
    return data
}

const addIngredientBtn = document.querySelector('#add-ingredient')
const ingredientsContainer = document.querySelector('.ingredients')
addIngredientBtn.addEventListener('click',async (e) => {
    const{ingredients, units} = await getIngredientsAndUnits() 
    const ingredientsField = document.createElement('div')
    ingredientsField.classList.add('ingredients-field')
    const ingredientsOptions = document.createElement('div')
    ingredientsOptions.classList.add('ingredients-options')
    const ingredientsOptionsContent = createOptions(ingredients)
    ingredientsOptions.appendChild(ingredientsOptionsContent)
    const input = document.createElement('input')
    input.type = 'number'
    input.placeholder = 'choose amount'
    input.classList.add('field')
    const unitsOptions = document.createElement('div')
    unitsOptions.classList.add('units-options')
    const unitsOptionsContent = createOptions(units)
    unitsOptions.appendChild(unitsOptionsContent)
    ingredientsField.appendChild(ingredientsOptions)
    ingredientsField.appendChild(input)
    ingredientsField.appendChild(unitsOptions)
    ingredientsContainer.appendChild(ingredientsField)
})

