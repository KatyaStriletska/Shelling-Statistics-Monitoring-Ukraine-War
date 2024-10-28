import "./index.css";
export default function ArticleComponent({text}){

    return (
        <div className="article-container">
            <div dangerouslySetInnerHTML={{ __html: text }} />
        </div>
    )
}