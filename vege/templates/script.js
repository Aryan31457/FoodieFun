const recipes = [
    { id: 1, name: 'Spaghetti Carbonara', description: 'A classic Italian pasta dish with eggs, cheese, and pancetta.', image: 'https://via.placeholder.com/300x200.png?text=Spaghetti+Carbonara' },
    { id: 2, name: 'Chicken Tikka Masala', description: 'A popular Indian curry dish with tender chicken in a creamy tomato sauce.', image: 'https://via.placeholder.com/300x200.png?text=Chicken+Tikka+Masala' },
    { id: 3, name: 'Caesar Salad', description: 'A crisp green salad with romaine lettuce, croutons, and a tangy dressing.', image: 'https://via.placeholder.com/300x200.png?text=Caesar+Salad' },
    { id: 4, name: 'Beef Stroganoff', description: 'A Russian dish of sautéed beef in a sour cream sauce, served over noodles.', image: 'https://via.placeholder.com/300x200.png?text=Beef+Stroganoff' },
    { id: 5, name: 'Vegetable Stir Fry', description: 'A quick and healthy mix of fresh vegetables cooked in a wok with Asian-inspired sauce.', image: 'https://via.placeholder.com/300x200.png?text=Vegetable+Stir+Fry' },
    { id: 6, name: 'Chocolate Chip Cookies', description: 'Classic American cookies with a perfect balance of sweet and chocolatey.', image: 'https://via.placeholder.com/300x200.png?text=Chocolate+Chip+Cookies' },
];

function createRecipeCard(recipe) {
    const card = document.createElement('div');
    card.className = 'recipe-card';
    card.innerHTML = `
        <img src="${recipe.image}" alt="${recipe.name}" class="recipe-image">
        <div class="recipe-content">
            <h3 class="recipe-title">${recipe.name}</h3>
            <p class="recipe-description">${recipe.description}</p>
            <div class="recipe-actions">
                <div class="action-buttons">
                    <button class="like-btn" data-id="${recipe.id}"><i class="fas fa-heart"></i> <span>0</span></button>
                    <button class="comment-btn" data-id="${recipe.id}"><i class="fas fa-comment"></i> <span>0</span></button>
                    <button class="share-btn" data-id="${recipe.id}"><i class="fas fa-share"></i></button>
                </div>
                <div class="edit-delete-buttons">
                    <button class="edit-btn" data-id="${recipe.id}"><i class="fas fa-edit"></i></button>
                    <button class="delete-btn" data-id="${recipe.id}"><i class="fas fa-trash"></i></button>
                </div>
            </div>
        </div>
    `;
    return card;
}

function renderRecipes() {
    const recipeGrid = document.getElementById('recipe-grid');
    recipeGrid.innerHTML = '';
    recipes.forEach(recipe => {
        const card = createRecipeCard(recipe);
        recipeGrid.appendChild(card);
    });
}

function handleLike(e) {
    if (e.target.classList.contains('like-btn') || e.target.closest('.like-btn')) {
        const btn = e.target.closest('.like-btn');
        const span = btn.querySelector('span');
        let likes = parseInt(span.textContent);
        span.textContent = likes + 1;
    }
}

function handleComment(e) {
    if (e.target.classList.contains('comment-btn') || e.target.closest('.comment-btn')) {
        const btn = e.target.closest('.comment-btn');
        const span = btn.querySelector('span');
        let comments = parseInt(span.textContent);
        span.textContent = comments + 1;
    }
}

function handleShare(e) {
    if (e.target.classList.contains('share-btn') || e.target.closest('.share-btn')) {
        alert('Sharing functionality would be implemented here.');
    }
}

function handleEdit(e) {
    if (e.target.classList.contains('edit-btn') || e.target.closest('.edit-btn')) {
        const btn = e.target.closest('.edit-btn');
        const recipeId = btn.getAttribute('data-id');
        alert(`Edit functionality for recipe ${recipeId} would be implemented here.`);
    }
}

function handleDelete(e) {
    if (e.target.classList.contains('delete-btn') || e.target.closest('.delete-btn')) {
        const btn = e.target.closest('.delete-btn');
        const recipeId = btn.getAttribute('data-id');
        if (confirm('Are you sure you want to delete this recipe?')) {
            alert(`Delete functionality for recipe ${recipeId} would be implemented here.`);
        }
    }
}

function handleAddRecipe() {
    alert('Add recipe functionality would be implemented here.');
}

function handleSearch() {
    const searchTerm = document.getElementById('search-input').value.toLowerCase();
    const filteredRecipes = recipes.filter(recipe => 
        recipe.name.toLowerCase().includes(searchTerm) || 
        recipe.description.toLowerCase().includes(searchTerm)
    );
    const recipeGrid = document.getElementById('recipe-grid');
    recipeGrid.innerHTML = '';
    filteredRecipes.forEach(recipe => {
        const card = createRecipeCard(recipe);
        recipeGrid.appendChild(card);
    });
}

document.addEventListener('DOMContentLoaded', () => {
    renderRecipes();
    
    const recipeGrid = document.getElementById('recipe-grid');
    recipeGrid.addEventListener('click', (e) => {
        handleLike(e);
        handleComment(e);
        handleShare(e);
        handleEdit(e);
        handleDelete(e);
    });

    const addRecipeBtn = document.getElementById('add-recipe-btn');
    addRecipeBtn.addEventListener('click', handleAddRecipe);

    const searchInput = document.getElementById('search-input');
    searchInput.addEventListener('input', handleSearch);
});

