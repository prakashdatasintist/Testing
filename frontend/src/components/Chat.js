import React from 'react';
import { useParams } from 'react-router-dom';

function Chat() {
  let { id } = useParams();

  return (
    <div>
      <h2>Chat with User {id}</h2>
      <div>
        {/* Chat implementation here */}
      </div>
    </div>
  );
}

export default Chat;
