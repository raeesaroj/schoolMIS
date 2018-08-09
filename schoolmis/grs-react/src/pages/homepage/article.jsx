import React, { Component } from 'react';
import { Icon } from 'react-materialize';

import './article.css';

class Article extends Component {
  render () {
    return (
      <div>
        <div className="row">
          <div className="col-md-6">
            <h1 className="article-head"><Icon>rss_feed</Icon> News & Notices</h1>
            <div className="article-div">
              <div className="article-date">
                <span>18</span><br />
                <span style={{ fontSize: '14px' }}>mar</span>
              </div>
              <a href="#!" className="article-des">Scout Inter Patrol Cooking Competition</a>
            </div>
            <div className="article-div">
              <div className="article-date">
                <span>20</span><br />
                <span style={{ fontSize: '14px' }}>mar</span>
              </div>
              <a href="#!" className="article-des">3rd Grand Finale of GRS Little Champs</a>
            </div>
          </div>
          <div className="col-md-6">
            <h1 className="article-head"><Icon>notifications</Icon> Upcoming Events</h1>
            <div className="article-div">
              <div className="article-date">
                <span>24</span><br />
                <span style={{ fontSize: '14px' }}>mar</span>
              </div>
              <a href="#!" className="article-des">Saturday, Holiday</a>
              <p className="article-content"></p>
            </div>
          </div>
        </div>

      </div>
    )
  }
}

export default Article;
