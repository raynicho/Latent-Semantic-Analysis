function [] = latent_semantic()
%get the document term matrix
filename = 'document_term_matrix.txt';
delimiterIn = '\t';
headerlinesIn = 0;
document_term_matrix = importdata(filename,delimiterIn,headerlinesIn);

%get the query vector
filename = 'query_vector.txt';
delimiterIn = ' ';
headerlinesIn = 0;
query_vector = importdata(filename,delimiterIn,headerlinesIn);


%Calculate the singular decomposition.
[U, S, V] = svd(document_term_matrix, 'econ');

%Transpose U and transpose V.
V = V';

%Calculate the rank matrices.
k = 2;
U_k = U(:, 1:k);
S_k = S(1:k, 1:k);
V_k = V(1:k, :);

%Find the new document vectors.
document_vector_coordinates = V_k;

%Find the new query vector.
query_new = query_vector'*U_k*inv(S_k);

%Pre-allocate space for the return matrix.
document_rank_matrix (1:k, 1) = 0;

%Get the number of columns in the document_vector_coordinates.
document_size = size(document_vector_coordinates);
document_size = document_size(2);

%Rank the documents and store in document_rank_matrix.
for x = 1:document_size
    document_rank_matrix(x,:) = dot(query_new', document_vector_coordinates(:, x))/(norm(query_new')*norm(document_vector_coordinates(:, x)));
end

google_average = mean(document_rank_matrix(1:10));
bing_average = mean(document_rank_matrix(11:20));
yahoo_average = mean(document_rank_matrix(21:30));

disp(google_average);
disp(bing_average);
disp(yahoo_average);
