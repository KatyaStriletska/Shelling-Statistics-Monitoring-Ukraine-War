import "./index.css";
export default function ArticleComponent({text}){

    return (
        <div className="article-container">
            <article>
               {text}
            </article>
        </div>
    )
}